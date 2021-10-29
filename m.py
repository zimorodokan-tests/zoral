output = []

def create_pages_links_list(list_of_elements):
	pages_links_list = []
	for link in list_of_elements:
		company_page_link = link.get_attribute("href")
		company_name = link.text
		print("company_page_link:", company_page_link)
		pages_links_list.append([company_name, company_page_link])
	print(pages_links_list)
	return pages_links_list

def append_data(data_list):
	output.append(data_list)
	print(data_list)
	print(output)
