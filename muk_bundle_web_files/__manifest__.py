###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    Odoo Proprietary License v1.0
#    
#    This software and associated files (the "Software") may only be used 
#    (executed, modified, executed after modifications) if you have
#    purchased a valid license from the authors, typically via Odoo Apps,
#    or if you have received a written agreement from the authors of the
#    Software (see the COPYRIGHT file).
#    
#    You may develop Odoo modules that use the Software as a library 
#    (typically by depending on it, importing it and using its resources),
#    but without copying any source code or material from the Software.
#    You may distribute those modules under the license of your choice,
#    provided that this license is compatible with the terms of the Odoo
#    Proprietary License (For example: LGPL, MIT, or proprietary licenses
#    similar to this one).
#    
#    It is forbidden to publish, distribute, sublicense, or sell copies of
#    the Software or modified copies of the Software.
#    
#    The above copyright notice and this permission notice must be included
#    in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###################################################################################

{
    "name": "MuK Web File Bundle",
    "summary": """New Features and UI Improvements""",
    "version": '11.0.1.0.0',   
    "category": 'Extra Tools',   
    "license": "OPL-1",
    "price": 5.00,
    "currency": 'EUR',
    "website": "https://www.mukit.at",
    "live_test_url": "https://demo.mukit.at/web/login",
    "author": "MuK IT",
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "depends": [
        "muk_utils",
        "muk_archive",
        "muk_converter",
        "muk_fields_lobject",
        "muk_web_utils",
        "muk_web_attachment_utils",
        "muk_web_export",
        "muk_web_export_attachment",
        "muk_web_fields_lobject",
        "muk_web_preview",
        "muk_web_preview_attachment",
        "muk_web_preview_audio",
        "muk_web_preview_csv",
        "muk_web_preview_image",
        "muk_web_preview_lobject",
        "muk_web_preview_mail",
        "muk_web_preview_markdown",
        "muk_web_preview_msoffice",
        "muk_web_preview_rst",
        "muk_web_preview_text",
        "muk_web_preview_vector",
        "muk_web_preview_video",
    ],
    "data": [
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}
