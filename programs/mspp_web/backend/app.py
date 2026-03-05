#!/usr/bin/env python3
"""
MSPP Data Plotter - Flask Backend API

This module serves a self-contained version of the MSPP web app.
To bypass strict corporate security that blocks .js files, this backend
inlines the JavaScript and CSS directly into the HTML on the fly.
"""

import logging
import os
import re
import tempfile
import traceback
from pathlib import Path

from flask import Flask, jsonify, request, send_file, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Import our custom logic
from .logic import DataProcessor, PlotGenerator, fig_to_base64

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Cross-platform path handling
BACKEND_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.abspath(os.path.join(BACKEND_DIR, '..', 'frontend', 'dist'))
TEMP_DIR = os.path.abspath(os.getenv('MSPP_TEMP_DIR', tempfile.gettempdir()))

app = Flask(__name__, static_folder=None)
CORS(app)

# Global instances
processor = DataProcessor()
plotter = PlotGenerator(processor)
uploaded_files = {}

def get_self_contained_html():
    """
    Reads index.html and inlines the JS and CSS files.
    This bypasses corporate security blocks on separate .js files.
    """
    html_path = os.path.join(STATIC_FOLDER, 'index.html')
    if not os.path.exists(html_path):
        return f"Error: index.html not found at {html_path}. Run 'npm run build' first."

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Find the JS bundle link tag
        js_tag_match = re.search(r'<script type="module" crossorigin src="/assets/(index-.*?\.js)"></script>', html)
        if js_tag_match:
            full_tag = js_tag_match.group(0)
            js_filename = js_tag_match.group(1)
            js_path = os.path.join(STATIC_FOLDER, 'assets', js_filename)
            
            if os.path.exists(js_path):
                with open(js_path, 'r', encoding='utf-8') as f:
                    js_code = f.read()
                # Use literal string replacement to avoid regex backslash issues
                html = html.replace(full_tag, f'<script type="module">{js_code}</script>')
                logger.info(f"Successfully inlined JS: {js_filename}")
            else:
                logger.warning(f"JS file not found: {js_path}")

        # 2. Find the CSS bundle link tag
        css_tag_match = re.search(r'<link rel="stylesheet" crossorigin href="/assets/(index-.*?\.css)">', html)
        if css_tag_match:
            full_tag = css_tag_match.group(0)
            css_filename = css_tag_match.group(1)
            css_path = os.path.join(STATIC_FOLDER, 'assets', css_filename)
            
            if os.path.exists(css_path):
                with open(css_path, 'r', encoding='utf-8') as f:
                    css_code = f.read()
                # Use literal string replacement
                html = html.replace(full_tag, f'<style>{css_code}</style>')
                logger.info(f"Successfully inlined CSS: {css_filename}")
            else:
                logger.warning(f"CSS file not found: {css_path}")

        return html
    except Exception as e:
        logger.error(f"Failed to generate self-contained HTML: {e}")
        return f"Internal Error: {str(e)}\n{traceback.format_exc()}"

@app.route('/')
@app.route('/<path:path>')
def serve_app(path=None):
    """
    Serves the inlined version of the app for all non-API routes.
    """
    if path and path.startswith('api/'):
        return jsonify({'error': 'Not found'}), 404
    
    logger.info("Serving self-contained HTML bundle")
    return Response(get_self_contained_html(), mimetype='text/html')

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok'})

@app.route('/api/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    files = request.files.getlist('files')
    temp_paths = []
    for file in files:
        if file and file.filename and file.filename.lower().endswith(('.tsv', '.txt')):
            safe_name = secure_filename(file.filename)
            temp_path = os.path.join(TEMP_DIR, safe_name)
            os.makedirs(os.path.dirname(temp_path), exist_ok=True)
            file.save(temp_path)
            uploaded_files[safe_name] = temp_path
            temp_paths.append(safe_name)
    return jsonify({'message': f'{len(temp_paths)} files uploaded successfully', 'files': temp_paths})

@app.route('/api/files', methods=['GET', 'DELETE'])
def manage_files():
    if request.method == 'DELETE':
        for path in uploaded_files.values():
            try: os.remove(path)
            except: pass
        uploaded_files.clear()
        if hasattr(processor, 'cached_data'):
            processor.cached_data = None
        return jsonify({'message': 'Cleared cache'})
    return jsonify({'files': list(uploaded_files.keys())})

@app.route('/api/plot/<chart_type>', methods=['POST'])
def generate_plot(chart_type):
    if not uploaded_files: return jsonify({'error': 'No files'}), 400
    try:
        data = processor.load_data(list(uploaded_files.values()))
        if chart_type == 'bar-chart': fig = plotter.create_bar_chart_figure(data)
        elif chart_type == 'sample-comparison': fig = plotter.create_comparison_figure(data)
        else: return jsonify({'error': 'Invalid plot type'}), 400
        return jsonify({'image': fig_to_base64(fig)})
    except Exception as e:
        logger.error(f"Plot generation failed: {e}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Server Error: {error}")
    return "500 Internal Server Error", 500

if __name__ == "__main__":
    port = int(os.getenv('FLASK_PORT', '5000'))
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    debug_mode = os.getenv('FLASK_ENV', 'production').lower() in ('development', 'debug')
    app.run(host=host, port=port, debug=debug_mode)
