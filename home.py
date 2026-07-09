HOME_TEMPLATE = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Sync</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="card">
            <div class="logo-wrap">
                <img class="logo" src="/static/Sync.png" alt="Sync logo">
            </div>
            <h2>Multitool & Utilities</h2>
            <p>Select an app:</p>
            <div class="version-list">
                <a class="version-link" href="{{ url_for('calculator', version='v2') }}">Calculator</a>
                <a class="version-link" href="{{ url_for('converter') }}">Unit Converter</a>
            </div>
        </div>
    </body>
</html>
"""
