import requests
from bs4 import BeautifulSoup

def scrape_data():
    # Fetch the HTML content from the URL
    response = requests.get("https://stellamaryscoe.edu.in/Management.php")
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all <div> tags with class "member-info"
    member_info_divs = soup.find_all("div", class_="member-info")

    # Initialize an empty list to store the positions and names
    positions_names = []

    # Iterate over each <div> element
    for div in member_info_divs:
        # Extract the text from the <h4> tag
        name = div.h4.get_text()
        # Extract the text from the <span> tag
        position = div.span.get_text()
        # Add the position and name to the list
        positions_names.append((position, name))

    # Fetch the HTML content from the "admin_desk.php" URL
    response = requests.get("https://stellamaryscoe.edu.in/admin_desk.php")
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all elements with class "font-weight-bold"
    bold_elements = soup.find_all(class_="font-weight-bold")

    # Iterate over each bold element
    for bold in bold_elements:
        # Get the name from the bold element
        name = bold.get_text()
        # If the name is "Dr.J.Jenix Rino"
        if name == "Dr.J.Jenix Rino":
            # Find the previous <h2> tag that precedes the bold element
            h2 = bold.find_previous("h2")
            # If the <h2> tag is found
            if h2:
                # Get the position from the <h2> tag
                position = h2.get_text()
        else:
            # Find the next <div> element with class "d-flex" that follows the bold element
            div = bold.find_next("div", class_="d-flex")
            # If the <div> element is found and it contains an <h2> tag
            if div and div.h2:
                # Get the position from the <h2> tag
                position = div.h2.get_text()
        # Add the position and name to the list
        positions_names.append((position, name))

    # Fetch the HTML content from the "facilities.php" URL
    response = requests.get("https://stellamaryscoe.edu.in/facilities.php")
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all <h5> elements with class "card-title"
    h5_elements = soup.find_all("h5", class_="card-title")

    # Initialize an empty list to store the facilities
    facilities = []

    # Iterate over each <h5> element
    for h5_element in h5_elements:
        # Find the <a> tag within the <h5> element
        a_tag = h5_element.find("a")
        # Extract the text content of the <a> tag
        text = a_tag.get_text(strip=True)
        # Add the text to the facilities list
        facilities.append(text)

    # Join the facilities into a single string with commas and spaces between them
    facilities_str = ", ".join(facilities)

    # Return the positions and names and the facilities
    return positions_names, facilities_str
if __name__ == "__main__":
    positions_names, facilities_str = scrape_data()
    print(positions_names)
    print(facilities_str)