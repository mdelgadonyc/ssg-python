# Static Site Generator (SSG)

A lightweight, easy-to-use static site generator built with Python. This SSG is designed to help developers quickly generate static HTML websites from Markdown files or plain text files.

## Features

- Convert Markdown files (`.md`) or plain text files (`.txt`) into static HTML.
- Generate static assets such as CSS and JS files.
- Lightweight and fast.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mdelgadonyc/ssg-python.git
    cd ssg-python
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt  # For Python
    ```

## Usage

1. Prepare your content:

    Place your `.md` or `.txt` files in the `content` directory. Ensure each file has a title in the front matter for metadata processing.

2. Build the static site:

    ```bash
    python ssg.py build  # For Python
    ```

3. The generated static files will be placed in the `dist` directory.

4. Preview your site:

    You can use any local server to preview the output. For example:

    ```bash
    python -m http.server 8000
    ```

    Open your browser and go to `http://localhost:8000`.

## Configuration

You can configure the static site generator using the `config.json` file located in the root directory. This includes options such as:

- **Input directory**: Where your content files are located.
- **Output directory**: Where the generated HTML files will be saved.
- **Template**: Path to your HTML templates for consistent site design.

## Example

Here's an example of a Markdown file with front matter:

```markdown
---
title: "Welcome to My Blog"
description: "This is the first post on my blog."
---

# Welcome!

This is the first post on my new blog, generated using this awesome Static Site Generator.
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Any improvements or features are welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy site building!
