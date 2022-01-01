/* -*- js -*-
 * versionwarning.js
 *
 * Display a warning box for obsolete doc versions, and add
 * <link rel=canonical> to lead search engines to the right place.
 *
 * Docs can include this in any script via
 *
 * var script = document.createElement("script"); script.type = "text/javascript"; script.src = "/doc/_static/versionwarning.js"; document.head.appendChild(script);
 *
 */

$(document).ready(function() {
    const pathPattern = /^\/doc\/()([0-9.]+)(.*)/;
    const latestStable = {
        "": "1.22"
    };
    const names = {
        "": "NumPy"
    };
    const getCanonicalUrl = (name, path) => {
        // Fixup Numpy URL for some pages known to be moved
        path = path.replace("/reference/generated/numpy.random.",
                            "/reference/random/generated/numpy.random.");
        return "https://numpy.org/doc/stable" + path;
    };
    const latestUrl = {
        "": "https://numpy.org/doc/stable/"
    };

    const showWarning = (msg) => {
        $('.body').prepend(
            '<p style="padding: 1em; border: 1px solid red; background: pink;" class="versionwarning">'
                + msg + '</p>');
    };
    const addCanonicalRel = (href) => {
        $('head').append(
            '<link rel="canonical" href="' + href + '"/>'
        );
    };

    const m = location.pathname.match(pathPattern);
    if (m !== null) {
        if ($('.versionwarning').length > 0) {
            return;
        }

        // Always add canonical rel tag
        const canonicalUrl = getCanonicalUrl(m[1], m[3]);
        addCanonicalRel(canonicalUrl);

        if (m[2] != latestStable[m[1]]) {
            // For obsolete versions, show a warning

            // Generate an URL for searching this page in stable docs, in
            // case the canonical URL is not valid
            let searchWords = document.title.replace(/—[^—]*$/, '').trim();
            if (!searchWords) {
                searchWords = document.title.trim();
            }
            const searchUrl = latestUrl[m[1]] + "search.html?q=" + encodeURI(searchWords);

            showWarning('This is documentation for an old release of '
                        + names[m[1]] + ' (version ' + m[2] + '). '
                        + '<span class="versionwarning-readlink">Read <a href="'
                        + canonicalUrl + '">this page</a></span> '
                        + '<span class="versionwarning-searchlink" style="display: none;">Search for <a href="'
                        + searchUrl + '">this page</a></span>'
                        + ' in the <a href="' + latestUrl[m[1]] + '">documentation of the '
                        + 'latest stable release</a> (version ' + latestStable[m[1]] + ').');

            // Check if the canonical page actually exists, and if not,
            // replace the direct link with a link to the search page
            $.ajax({
                url: canonicalUrl,
                cache: true
            }).fail(function (jqXHR, textStatus) {
                $('.versionwarning-readlink').attr('style', 'display: none;');
                $('.versionwarning-searchlink').attr('style', 'display: inline;');
            });
        }
    }
});
