template = {
	'format': 'A4',# STR_VALUE 'A4' OR 'letter'
	'unit': 'cm',# STR_VALUE 'cm' OR 'in'
	'top_margin': 1.,# FLOAT_VALUE
	'bottom_margin': 1.,# FLOAT_VALUE
	'left_margin': 1.,# FLOAT_VALUE
	'right_margin': 1.,# FLOAT_VALUE
	'column_number': 12,# INT_VALUE
	'row_number': 16,# INT_VALUE
	'row_gutter_size': 0.42,# FLOAT_VALUE
	'column_gutter_size': 0.42,# FLOAT_VALUE
	'body_margin_column': (2,1),# (INT_VALUE,INT_VALUE) # how many columns and gutters to count as margins left and right
	'cover_margin_color':'#FFFFFF',# STR_VALUE # HEX color as a String
	'cover_body_color':'#FFFFFF',# STR_VALUE # HEX color as a String
	'highlight_color':'#000000',# STR_VALUE # HEX color as a String
	'photo_rows': (9,9),# (INT_VALUE,INT_VALUE) # how many rows and gutters counting from top margin
	'divider_length': (2,3),# (INT_VALUE, INT_VALUE) # how many rows and gutters from left border of the photo
	'divider_thickness': 0.3,# FLOAT_VALUE in pt
	'divider_color': '#EEEEEE',# STR_VALUE # HEX color as a String
	'block_text_margin': (0,1),# (INT_VALUE,INT_VALUE) # how many rows and gutters text margin left and right within a block
	'block_title_align': (1,0),# (INT_VALUE,INT_VALUE) # how many rows and gutters  bottom alignment of block title from top border
	'block_background_color': '#EEEEEE',# STR_VALUE # HEX color as a String
	'block_title_color': '#000000',# STR_VALUE # HEX color as a String
	'block_title_font': 'Roboto-Medium.ttf',# FILE_PATH # filepath to a *.ttf file
	'block_title_size': 12, # INT_VALUE # font size pt
	'block_title_case': 'UPPERCASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE' ,'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'block_subtitle_color': '#959595',# STR_VALUE # HEX color as a String
	'block_subtitle_font': 'Roboto-Medium.ttf',# FILE_PATH # filepath to a *.ttf file
	'block_subtitle_size': 12, # INT_VALUE # font size pt
	'block_subtitle_case': 'TITLECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE','SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'block_title_line_height': 14.0, # FLOAT_VALUE line height pt for title and subtitle
	'block_title_spacing': (0,1),# (INT_VALUE,INT_VALUE) how many rows and gutters spacing between subtitle and description text
	'block_description_color': '#959595',# STR_VALUE # HEX color as a String
	'block_description_font': 'Roboto-Regular.ttf',# FILE_PATH # filepath to a *.ttf file
	'block_description_size': 10, # INT_VALUE # font size pt
	'block_description_line_height': 11., # FLOAT_VALUE line height pt for description text
	'block_description_align': 'JUSTIFY', # STR_VALUE 'ALIGN_LEFT', 'ALIGN_RIGHT' or 'JUSTIFY'
	'block_description_case': 'SENTENCECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'block_info_size': (3,2),# (INT_VALUE,INT_VALUE) # how many rows and gutters
	'block_info_class_color': '#959595',# STR_VALUE # HEX color as a String
	'block_info_data_color': '#000000',# STR_VALUE # HEX color as a String
	'block_info_class_font': 'Roboto-Regular.ttf',# FILE_PATH # filepath to a *.ttf file
	'block_info_class_case': 'TITLECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'block_info_data_font': 'Roboto-Regular.ttf',# FILE_PATH # filepath to a *.ttf file
	'block_info_class_size': 10, # INT_VALUE # font size pt
	'block_info_data_size': 10, # INT_VALUE # font size pt
	'block_info_line_height': 14., # FLOAT_VALUE line height pt 
	'block_info_data_case': 'LOWERCASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE','SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'pagination_font': 'Roboto-Light.ttf',# FILE_PATH # filepath to a *.ttf file
	'pagination_line_height': 8., # FLOAT_VALUE line height pt 
	'pagination_size': 6, # INT_VALUE # font size pt
	'pagination_case': 'TITLECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'pagination_color': '#CCCCCC',# STR_VALUE # HEX color as a String
	'cv_category_font':'Roboto-Medium.ttf',# FILE_PATH # filepath to a *.ttf file
	'cv_category_size': 12, # INT_VALUE # font size pt
	'cv_category_color': '#959595',# STR_VALUE # HEX color as a String
	'cv_category_case': 'UPPERCASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE','SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'cv_category_line_height': 14., # FLOAT_VALUE line height
	'cv_category_spacing': (0,2),# (INT_VALUE,INT_VALUE) # how many rows and gutters spacing between categories and cv title
	'cv_date_font':'Roboto-Regular.ttf',# FILE_PATH # filepath to a *.ttf file
	'cv_date_size': 11, # INT_VALUE # font size pt
	'cv_date_color':'#959595',# STR_VALUE # HEX color as a String
	'cv_title_font': 'Roboto-Light.ttf',# FILE_PATH # filepath to a *.ttf file
	'cv_title_size': 11, # INT_VALUE # font size pt
	'cv_title_color': '#000000',# STR_VALUE # HEX color as a String
	'cv_title_case': 'UPPERCASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'cv_subtitle_font': 'Roboto-LightItalic.ttf',# FILE_PATH # filepath to a *.ttf file
	'cv_subtitle_size': 11, # INT_VALUE # font size pt
	'cv_subtitle_color': '#000000',# STR_VALUE # HEX color as a String
	'cv_subtitle_case': 'TITLECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'cv_detail_font': 'Roboto-LightItalic.ttf',# FILE_PATH # filepath to a *.ttf file
	'cv_detail_size': 11, # INT_VALUE # font size pt
	'cv_detail_color': '#959595',# STR_VALUE # HEX color as a String
	'cv_detail_case': 'SENTENCECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'cv_title_line_height': 12, # INT_VALUE # font size pt
	'cv_highlight_color': '#EEEEEE',# STR_VALUE # HEX color as a String
	'cv_title_spacing': (0,1),# (INT_VALUE,INT_VALUE) # how many rows and gutters spacing between subtitle and description text
	'cv_description_font':'Roboto-Regular.ttf',# FILE_PATH # filepath to a *.ttf file
	'cv_description_size': 11, # INT_VALUE # font size pt
	'cv_description_color': '#000000',# STR_VALUE # HEX color as a String
	'cv_description_case': 'SENTENCECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'cv_description_align': 'JUSTIFY', # STR_VALUE 'ALIGN_LEFT', 'ALIGN_RIGHT' or 'JUSTIFY'
	'cv_margin_color': '#FFFFFF',# STR_VALUE # HEX color as a String
	'cv_body_color': '#FFFFFF',# STR_VALUE # HEX color as a String
	'letter_date_font':'Roboto-LightItalic.ttf',# FILE_PATH # filepath to a *.ttf file
	'letter_date_color': '#000000',# STR_VALUE # HEX color as a String
	'letter_date_size': 11, # INT_VALUE # font size pt
	'letter_date_case': 'LOWERCASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'letter_date_spacing': (1,0),# (INT_VALUE,INT_VALUE) # how many rows and gutters spacing between date and top border, also below to recipient
	'letter_date_left_margin': (1,0),# (INT_VALUE,INT_VALUE) # how many columns and gutters
	'letter_receiver_font':'Roboto-Light.ttf',# FILE_PATH # filepath to a *.ttf file
	'letter_receiver_size': 11, # INT_VALUE # font size pt
	'letter_receiver_color': '#000000',# STR_VALUE # HEX color as a String
	'letter_receiver_case': 'UPPERCASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'letter_receiver_line_height': 12, # INT_VALUE # font size pt
	'letter_receiver_bottom_margin': (0,1),# (INT_VALUE,INT_VALUE) # how many rows and gutters 
	'letter_text_spacing': (1,0),# (INT_VALUE,INT_VALUE) # how many rows and gutters to place the bottom position of the first text line from the top border
	'letter_text_font':'Roboto-Regular.ttf',# FILE_PATH # filepath to a *.ttf file
	'letter_text_size': 11, # INT_VALUE # font size pt
	'letter_text_color': '#000000',# STR_VALUE # HEX color as a String
	'letter_text_line_height': 12, # INT_VALUE # font size pt
	'letter_text_align': 'JUSTIFY', # STR_VALUE 'ALIGN_LEFT', 'ALIGN_RIGHT' or 'JUSTIFY'
	'letter_text_case': 'SENTENCECASE', # STR_VALUE 'UPPERCASE', 'LOWERCASE', 'SENTENCECASE' or 'TITLECASE' (first letter of each word in UPPERCASE and the rest in LOWERCASE) font case as a string
	'letter_block_color': '#FFFFFF',# STR_VALUE # HEX color as a String
	'letter_margin_color': '#EEEEEE',# STR_VALUE # HEX color as a String
	'letter_body_color': '#EEEEEE',# STR_VALUE # HEX color as a String
}