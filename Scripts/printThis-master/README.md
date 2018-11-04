#printThis
Printing plug-in for jQuery

## Features
* Print specific & multiple DOM elements
* Preserve page CSS/styling
** or add new CSS; the world is your oyster!
* Preserve form entries
* **1.9.0 adds experimental canvas support**

## Usage
### Basic
```javascript
$('selector').printThis();
```

### Advanced Features
```javascript
$('#kitty-one, #kitty-two, #kitty-three').printThis({
    importCSS: false,
    loadCSS: "",
    header: "<h1>Look at all of my kitties!</h1>"
});
```

#### debug
Debug leaves the iframe visible on the page after `printThis` runs, allowing you to inspect the markup and CSS.

#### importCSS
Copy CSS `<link>` tags to the printThis iframe. On by default.

#### importStyle
Copy CSS `<style>` tags to the printThis iframe. Off by default.

#### printContainer
Includes the markup of the selected container, not just its contents. On by default.

#### loadCSS
Provide a URL for an additional stylesheet to the printThis iframe. Empty string (off) by default.

#### pageTitle
Use a custom page title on the iframe. This may be reflected on the printed page, depending on settings. Blank by default.

#### removeInline
Eliminates any inline style attributes from the content. Off by default.

#### printDelay
The amount of time to wait before calling `print()` in the printThis iframe. Defaults to 333 milliseconds.
Appropriate values depend heavily on the content and network performance. Graphics heavy, slow, or uncached content may need extra time to load.

#### header & footer
A string or jQuery object to prepend or append to the printThis iframe content. `null` by default.

```javascript
$('#mySelector').printThis({
    header: "<h1>Amazing header</h1>"
});
 
$('#mySelector').printThis({
    footer: $('.hidden-print-header-content')
});
```

As of 1.9.1, jQuery objects will be cloned rather than moved.

#### base
The `base` option allows several behaviors.
By default it is `false`, meaning a the current document will be set as the base URL.  

If set to `true`, a `<base>` attribute will be set if one exists on the page. 
If none is found, the tag is omitted, which may be suitable for pages with Fully Qualified URLs.

When passed as a string, it will be used as the `href` attribute of a `<base>` tag.

#### formValues
This setting attempts to copy the current values of form elements into the printThis iframe. On by default.

Complex field values, such as those containing quotations or mark-up, may have difficulties. Please report any unexpected behavior.

#### canvas -- Experimental
As of 1.9.0 you may be able to duplicate canvas elements to the printThis iframe. Disabled by default.
This has received only limited testing and so may not work in all browsers and situations.

#### doctypeString
A doctype string to use on the printThis iframe. Defaults to the HTML5 doctype.

#### removeScripts
Deletes script tags from the content to avoid errors or unexpected behavior during print.

### All Options
```javascript
$("#mySelector").printThis({
    debug: false,               // show the iframe for debugging
    importCSS: true,            // import page CSS
    importStyle: false,         // import style tags
    printContainer: true,       // grab outer container as well as the contents of the selector
    loadCSS: "path/to/my.css",  // path to additional css file - use an array [] for multiple
    pageTitle: "",              // add title to print page
    removeInline: false,        // remove all inline styles from print elements
    printDelay: 333,            // variable print delay; depending on complexity a higher value may be necessary
    header: null,               // prefix to html
    footer: null,               // postfix to html
    base: false ,               // preserve the BASE tag, or accept a string for the URL
    formValues: true,           // preserve input/form values
    canvas: false,              // copy canvas elements (experimental)
    doctypeString: "...",       // enter a different doctype for older markup
    removeScripts: false        // remove script tags from print content
});
```

## Please read
* "It's not working" without any details is not a valid issue and will be closed
* A url, or html file, is necessary to debug. Due to the complexities of printing and this plugin, an example is the best way to debug
* When troubleshooting, set `debug: true` and inspect the iframe. Please report your findings when reporting an issue
* Every user should be active in the debugging process

## ToDo:
* Look at more efficient form field value persist
* Look at alternative to setTimeout ($.deferred?)
              


