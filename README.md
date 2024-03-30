# Data Commons

[Data Commons Goals Built (dist)](dist/) and [Raw Files showing Javascript (docs)](docs/)

**Root of UN Goals nav from Google API:** - [Start here as we automate SDG Goal visualization](https://datacommons.org/tools/statvar#s=dc%2Fs%2FUnitedNationsUn&d=dc%2Fd%2FUnitedNationsUn_SdgIndicatorsDatabase)
TO DO: Simplify and save the UN Goal navigation as a json file for our filters.

[Data Loader](https://observablehq.com/framework/loaders) - Save frequent requests as static files. (Good for simplified UN Goals navigation.)

---

This is an [Observable Framework](https://observablehq.com/framework) project. 
Run once daily when you start - updates dependencies defined in [package.json](package.json):

	yarn install

To build - this pulls from APIs and outputs from "[docs](docs)" to static files in "[dist](dist)":

	yarn build

The following is an alternative to using `yarn dev` (which you'd use if only viewing dist)

This setup allows you to view multiple repos in one webroot.
If you haven't yet, start an http server in your webroot, external to the data-commons folder.

	cd ../ && python -m http.server 8887

If you haven't yet, pull down the [localsite repo](https://github.com/modelearth/localsite).
This provides navigation when you view src files in the "[docs](docs)" folder.

	git clone https://github.com/modelearth/localsite localsite &&
	cd data-commons

Then visit the following to view:
<http://localhost:8887/data-commons/dist>
<http://localhost:8887/data-commons/docs>

Turn on GitHub Pages for both repos so we can preview changes.


For more, see <https://observablehq.com/framework/getting-started>.

## Project structure

In our project, folders for components and data reside in multiple "goal" folders:

```ini
data-commons
├─ README.md
├─ docs
│  ├─ space
│  │  ├─ components
│  │  │ 	└─ timeline.js     # an importable module
│  │  ├─ data
│  │  │ 	└─ events.json     # a static data file
│  │  └─ launches.csv.js       # a data loader
│  ├─ jobs
│  ├─ transit
│  ├─ innovation
│  ├─ education
│  ├─ economy
│  ├─ index.html               # a localsite page visible in docs
│  └─ index.md                 # a dist page
├─ dist
├─ observablehq.config.ts      # the project config file
├─ package.json
└─ .gitignore
```

**`docs`** - This is the “source root” — where your source files live. Pages go here. Each page is a Markdown file. Observable Framework uses [file-based routing](https://observablehq.com/framework/routing), which means that the name of the file controls where the page is served. You can create as many pages as you like. Use folders to organize your pages.

**`docs/index.md`** - This is the home page for your site. You can have as many additional pages as you’d like, but you should always have a home page, too.

**`docs/data`** - You can put [data loaders](https://observablehq.com/framework/loaders) or static data files anywhere in your source root, but we recommend putting them here.

**`docs/components`** - You can put shared [JavaScript modules](https://observablehq.com/framework/javascript/imports) anywhere in your source root, but we recommend putting them here. This helps you pull code out of Markdown files and into JavaScript modules, making it easier to reuse code across pages, write tests and run linters, and even share code with vanilla web applications.

**`observablehq.config.ts`** - This is the [project configuration](https://observablehq.com/framework/config) file, such as the pages and sections in the sidebar navigation, and the project’s title.

## Command reference

| Command           | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `yarn install`            | Install or reinstall dependencies                        |
| `yarn dev`        | Start local preview server                               |
| `yarn build`      | Build your static site, generating `./dist`              |
| `yarn deploy`     | Deploy your project to Observable                        |
| `yarn clean`      | Clear the local data loader cache                        |
| `yarn observable` | Run commands like `observable help`                      |
