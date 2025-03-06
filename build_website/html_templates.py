template_terminal = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/styles.css">
</head>

<body>
    <img src="/logos/trauma_logo.jpeg" alt="generic_logo" class="logo">
    <h1>{title}</h1>
    <button onclick="location.href='/index.html'">Back to Home</button>
    <button onclick="location.href='/{lastpage_path}'">Back to {lastpage}</button>
    {content}
</body>

</html>
"""

template_terminal_home_is_lastpage = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/styles.css">
</head>

<body>
    <img src="/logos/trauma_logo.jpeg" alt="generic_logo" class="logo">
    <h1>{title}</h1>
    <button onclick="location.href='/index.html'">Back to Home</button>
    {content}
</body>

</html>
"""

template_intermediate = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/styles.css">
</head>

<body>
    <img src="/logos/trauma_logo.jpeg" alt="generic_logo" class="logo">
    <h1>{title}</h1>
    <button onclick="location.href='/index.html'">Back to Home</button>
    <button onclick="location.href='/{lastpage_path}'">Back to {lastpage}</button>
    {content}
</body>

</html>
"""

template_intermediate_home_is_lastpage = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/styles.css">
</head>

<body>
    <img src="/logos/trauma_logo.jpeg" alt="generic_logo" class="logo">
    <h1>{title}</h1>
    <button onclick="location.href='/index.html'">Back to Home</button>
    {content}
</body>

</html>
"""

template_button = """<button onclick="location.href='/{path}'">{text}</button>"""

# get rid of absolute path here for path so that it goes to website referenced
template_button_csv = """<button onclick="location.href='{path}'">{text}</button>"""

from string import Template

index_template = Template("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TRAUMA GUIDELINES</title>
    <link rel="manifest" href="/manifest.json">
    <link rel="stylesheet" href="/styles.css">
    <meta name="theme-color" content="#333333">
    <link rel="apple-touch-icon" href="/logos/trauma_logo.jpeg">
</head>

<body>
    <img src="/logos/trauma_logo.jpeg" alt="generic_trauma_logo" class="logo">
    <h1 class="center">TRAUMA GUIDELINES</h1>
    <p class="center">These guidelines utilize best clinical practices but are not a substitute for individual
        judgement.</p>
    <div class="search-container">
        <input type="text" id="search" placeholder="Search guidelines..." oninput="searchGuidelines()">
    </div>
    <div id="search-results" class="search-results"></div>
    <div class="button-container" id="button-container">${content}
    </div>
    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('service-worker.js')
                .then(registration => {
                    console.log('ServiceWorker registration successful with scope: ', registration.scope);
                })
                .catch(error => {
                    console.log('ServiceWorker registration failed: ', error);
                });
        }

        let debounceTimeout;
        const debounceDelay = 300;

        async function searchGuidelines() {
            clearTimeout(debounceTimeout);
            debounceTimeout = setTimeout(async () => {
                const query = document.getElementById('search').value.toLowerCase();
                const resultsContainer = document.getElementById('search-results');
                const buttonContainer = document.getElementById('button-container');
                resultsContainer.innerHTML = ''; // Clear previous results

                if (!query) {
                    buttonContainer.style.display = 'block'; // Show buttons if no query
                    return;
                }

                const response = await fetch('search-index.json');
                const pages = await response.json();

                const regex = new RegExp(`(${query})`, 'gi');

                let hasResults = false;

                pages.forEach(page => {
                    const textMatch = page.text.toLowerCase().includes(query);

                    if (textMatch) {
                        hasResults = true;
                        const highlightedText = page.text.replace(regex, '<span class="highlight">$1</span>');

                        const resultItem = document.createElement('div');
                        resultItem.className = 'result-item';
                        resultItem.innerHTML = `
                            <div><a href="${page.url}">${highlightedText}</a></div>
                        `;

                        resultsContainer.appendChild(resultItem);
                    }
                });

                if (hasResults) {
                    buttonContainer.style.display = 'none'; // Hide buttons if there are search results
                } else {
                    buttonContainer.style.display = 'block'; // Show buttons if no search results
                }
            }, debounceDelay);
        }

        document.getElementById('search').addEventListener('input', searchGuidelines);
    </script>
</body>

</html>""")