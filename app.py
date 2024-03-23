import tkinter as tk
import webbrowser
from libgen_api import LibgenSearch

def search_book():
    query = entry.get()
    if query:
        try:
            libgen = LibgenSearch()
            results = libgen.search_title(query)
            if results:
                download_links = []
                for idx, result in enumerate(results[:20], 1):  # Limit to the first 20 results
                    for key in ['Mirror_1', 'Mirror_2', 'Mirror_3']:
                        if key in result:
                            download_links.append(f"{idx}. {result[key]}")
                if download_links:
                    download_links_text = "\n".join(download_links)
                    text.delete('1.0', tk.END)  # Clear previous content
                    text.insert(tk.END, download_links_text)
                    set_hyperlinks(text, download_links)
                else:
                    text.delete('1.0', tk.END)  # Clear previous content
                    text.insert(tk.END, "No download links found for the given book.")
            else:
                text.delete('1.0', tk.END)  # Clear previous content
                text.insert(tk.END, "No results found for the given book.")
        except Exception as e:
            text.delete('1.0', tk.END)  # Clear previous content
            text.insert(tk.END, f"Error: {str(e)}")
    else:
        text.delete('1.0', tk.END)  # Clear previous content
        text.insert(tk.END, "Please enter a book name.")

def set_hyperlinks(widget, links):
    widget.tag_configure("hyperlink", foreground="blue", underline=1)
    for idx, link in enumerate(links, 1):
        widget.tag_add(f"hyperlink_{idx}", f"{idx}.0", f"{idx}.end")
        widget.tag_bind(f"hyperlink_{idx}", "<Button-1>", lambda event, url=link.split()[1]: open_hyperlink(url))

def open_hyperlink(url):
    webbrowser.open_new(url)

# Create the main window
root = tk.Tk()
root.title("Book Downloader")

# Create a label and entry widget for the book name
label = tk.Label(root, text="Enter Book Name:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the search
search_button = tk.Button(root, text="Search", command=search_book)
search_button.pack()

# Create a Text widget to display the download links
text = tk.Text(root)
text.pack()

# Run the main event loop
root.mainloop()
