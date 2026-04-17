# css-rotator

Utility to rotate css-theme of my webblog either via cron-job or via github-actions-ui (workflow-dispatch).

## Install and setup

Install as submodule in you github-pages-blog and move the workflow-file to `.github/workflows` to activate it.

```sh
git submodule add <path> css-rotator
cp css-rotator/workflow/weekly-rotation.yml .github/workflows/
```

In `.github/workflows/weekly-rotation.yml` change the env-var for the path to the variables.css.

```
# ...
CSS_VAR_PATH: "../themes/your-theme/path/to/variables.css" # CHANGE 
# ...
```

# How to use

In your `style.css` import the variables.css via `@import "path/to/variables.css";`
Now you can to use the variables defined in variables.css as attributes in your style css.

For example if your template for variables.css looks loke this:

```css
:root {
  --bg: #4A2626; 
  --h1: #D93A3A;
  --h2: #a09f93;
  --text: #FFFFFF; 
  --accent: #F2C94C;
  --code-bg: #0A0808;
}
```

you could set your colors as `var(--<variable-name>)`. Here an example to set the background-color and text-color:

```css
html {
  background-color: var(--bg);
  color:            var(--text);
}
```