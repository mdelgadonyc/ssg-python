# Static Site Generator (SSG)

A lightweight, easy-to-use static site generator (SSG) built with Python. This SSG is designed to help developers quickly generate static HTML websites from Markdown files.

## Features

- Converts Markdown files (`.md`) into static HTML pages.
- Recursively processes all Markdown files in `content`, generating HTML files in the corresponding folder structure within `public`.
- Copies all static files from the `static` directory to the `public` directory.
- Lightweight and fast, ideal for small sites.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mdelgadonyc/ssg-python.git
    cd ssg-python
    ```

## Usage

1. **Prepare your content**:

    - Place your `.md` files in the `content` directory. Each file should have a title in Markdown header format (`# Title`) at the top for processing.
    - Store any images, CSS, or other static files in the `static` directory.

2. **Build the static site**:

    ```bash
    ./main.sh
    ```

    - This will generate the static HTML files in the `public` directory. Each `.md` file in `content` will be processed, and the resulting `.html` file will be saved in `public`, mirroring the directory structure of `content`.

3. **Preview your site**:

    - The project serves the generated HTML pages on `localhost` at port `8888` by default. While `main.sh` is running, you can open your browser and navigate to `http://localhost:8888` to preview the site.

## Example

This project includes sample files to get you started:

- **Markdown files**: `index.md` in the root of `content` and another `index.md` in `content/majesty`.
- **Static assets**: An image (`rivendell.png`) and a CSS file (`index.css`) in `static`.

The generated HTML pages will be saved in `public/index.html` and `public/majesty/index.html`, respectively.

## Directory Structure

After running `./main.sh`, your project structure should look like this:

    ssg-python/
    ├── content/
    │   ├── index.md
    │   └── majesty/
    │       └── index.md
    ├── public/
    │   ├── index.html
    │   ├── majesty/
    │   │   └── index.html
    │   ├── images/
    │   │   └── rivendell.png
    │   └── index.css
    ├── static/
    │   ├── images/
    │   │   └── rivendell.png
    │   └── index.css
    ├── template.html
    └── main.sh

## Troubleshooting

- **File Permissions**: Ensure `main.sh` has executable permissions. You may need to run `chmod +x main.sh` before running the script.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy site building!
