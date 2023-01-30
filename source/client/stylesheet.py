css = """
    QWidget {
        font-size: 14px;
        font-family: Arial;
    }

    QWidget#background {
        background: rgba(255, 255, 255, 1);
        border-radius: 10px;
    }
    QWidget#getstart_box {
        background: rgba(255, 255, 255, 1);
        border-radius: 7px;
    }
    
    QWidget#titlebar {
        background: transparent;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
    }
    
    QPushButton {
        font-size: 14px;
    }
    QPushButton#search_button {
        
        border: none;
    }
    QPushButton#exit_button {
        background: transparent;
        border-image: url(./image/gui/close.png) 0 0 0 0 stretch stretch; 
        border: none;
    }
    QLabel#info_text {
        font-size: 15px;
        font-family: Open Sans SemiCondensed Medium;
        color: blue;
    }

    QPushButton#exit_button:hover {
        border-image: url(./image/gui/close_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#exit_button:pressed {
        border-image: url(./image/gui/close_pressed.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#exit_button:disabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button {
        background: transparent;
        border-image: url(./image/gui/minimize.png) 0 0 0 0 stretch stretch; 
        border: none;
    }

    QPushButton#minimize_button:hover {
        border-image: url(./image/gui/minimize_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button:pressed {
        border-image: url(./image/gui/minimize_pressed.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button:disabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button {
        background: transparent;
        border-image: url(./image/gui/fullscreen.png) 0 0 0 0 stretch stretch; 
        border: none;
    }

    QPushButton#fullscreen_button:hover {
        border-image: url(./image/gui/fullscreen_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button:pressed {
        border-image: url(./image/gui/fullscreen_pressed.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button:!enabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#main_button {
        font-size: 15px;
        font-family: San Francisco Display Black;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0.3,
            stop: 0 #07efeb,
            stop: 0.2 #1ec4dc,
            stop: 0.4 #369acd,
            stop: 0.6 #4d6fbe,
            stop: 0.8 #6644af);
        border: none;
        border-radius: 10px;
    }

    QPushButton#main_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0.3,
            stop: 0 #CFF4D2,
            stop: 0.2 #7BE495,
            stop: 0.4 #56C596,
            stop: 0.6 #329D9C,
            stop: 0.8 #205072 );
    }

    QPushButton#main_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0.3,
            stop: 0 #6644af,
            stop: 0.2 #4d6fbe,
            stop: 0.4 #369acd,
            stop: 0.6 #1ec4dc,
            stop: 0.8 #07efeb );
    }
     QPushButton#main_button1 {
        font-size: 15px;
        font-family: San Francisco Display Black;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0.3,
            stop: 0 #CFF4D2,
            stop: 0.2 #7BE495,
            stop: 0.4 #56C596,
            stop: 0.6 #329D9C,
            stop: 0.8 #205072 );
        border: none;
        border-radius: 10px;
    }

    QPushButton#main_button1:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0.3,
            stop: 0 #07efeb,
            stop: 0.2 #1ec4dc,
            stop: 0.4 #369acd,
            stop: 0.6 #4d6fbe,
            stop: 0.8 #6644af);
    }

    QPushButton#main_button1:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0.3,
            stop: 0 #6644af,
            stop: 0.2 #4d6fbe,
            stop: 0.4 #369acd,
            stop: 0.6 #1ec4dc,
            stop: 0.8 #07efeb );
    }


    QPushButton#forgotpw-register-login {
        background: transparent;
        color: darkblue;
        border: none;
    }

    QPushButton#more_info {
        background: transparent;
        color: darkblue;
        border: none;
    }

    QPushButton#forgot_password-register:hover {
        color: purple;
    }

    QLabel#main_label {
        font-size: 20px;
        font-family: junegull;
        color: #02055A;
    }
    QLabel#hello {
        background: white;
        font-size: 12px;
        font-family: San Francisco Display;
        color: black;    
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;    
    }
    QLabel#svaddrtag {
        border-radius: 0px;
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px;
        background: white;
        font-size: 14px;
        color: black;
        font-family: San Francisco Display Bold;
        background: rgb(235, 235, 235);
    }
    QLabel#product_image {
        background: white;
        border-image: url(./image/gui/login_picture.jpg) 0 0 0 0 stretch stretch;
        border-radius: 0px;
        border-top-right-radius: 10px;
        border-top-left-radius: 10px;
        border-bottom-right-radius: 10px;
        border-bottom-left-radius: 10px;
    }
    QLabel#ads_title {
        background: white;
        font-size: 20px;
        font-family: junegull;
        color: #043087;
        background: rgb(235, 235, 235);
        border-radius: 5px;
        border-top-right-radius: 10px;
        border-top-left-radius: 10px;
        border-bottom-right-radius: 10px;
        border-bottom-left-radius: 10px;
    }
    
    QLineEdit {
        font-size: 15px; 
        background: rgba(220, 220, 220, 1); 
        border: 0px solid #bababa; 
        border-radius: 20px; 
        padding-left: 15px;
    }

    QLineEdit:focus {
        border: 2px solid rgb(120, 120, 255);
        padding-left: 13px;
    }
    
    QWidget#login_box, QWidget#register_box, QWidget#forgotpw_box {
        background: white;
    }

    QComboBox {
        font-size: 15px;
        background: rgb(220, 220, 220);
        border: none;
        border-radius: 20px;
        padding-left: 15px;
    }

    QComboBox::drop-down {
        background: transparent;
        border: none;
        border-radius: 20px;
        width: 40px;
    }

    QComboBox::down-arrow {
        image: url(./image/gui/down-arrow.png);
    }
"""

basegui = """
    QWidget {
        font-size: 14px;
        font-family: Arial;
    }

    QWidget#container {
        background: rgba(220, 220, 220, 1);
        border-radius: 5px;
    }
    QWidget#background {
        background: rgba(220, 220, 220, 1);
        border-radius: 10px;
    }

    QWidget#messagebox_container {
        background: rgb(235, 235, 235);
        border-radius: 5px;
        border-bottom-left-radius: 10px;
    }
    QWidget#search_container {
        background: rgb(235, 235, 235);
        border-radius: 10px;
    }
    QWidget#titlebar {
        font-size: 16px;
        color: rgb(50, 50, 50);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(229, 229, 229),
            stop: 1 rgb(205, 205, 205));
        border-top: 1px solid rgb(244, 244, 244);
        border-bottom: 1px solid rgb(167, 167, 167);
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
    }

    QWidget#profile_popup {
        background: rgba(255, 255, 255, 0.85);
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
    }

    QWidget#profile_popup QLabel#profile_fullname {
        font-size: 16px;
    }

    QWidget#profile_popup QLabel#profile_username {
        color: gray;
        font-size: 14px;
        font-style: italic;
    }

    QWidget#profile_popup QPushButton {
        background: white;
        font-size: 12px;
    }

    QWidget#sidebar {
        background: rgb(236, 236, 236);
        border-right: 1px solid rgb(200, 200, 200);
        border-bottom-left-radius: 10px;
    }

    QWidget#sidebar QLineEdit#searchbox {
        border: none;
        font-size: 15px;
        background: rgb(240, 240, 240);
        padding-left: 5px;
        border-radius: none;
    }
    
    QWidget#sidebar QLineEdit#searchbox:focus {
        background: white;
        border: none;
    }

    QWidget#sidebar QLineEdit#searchbox QPushButton#search_clear {
        background: url(./image/gui/clear.png);
        border: none;
    }

    QLineEdit, QTextEdit {
        font-size: 13px;
        background: white;
        font-size: 14px;
        border: 1px solid rgb(179, 179, 179);
        border-radius: 6px;
        padding: 3px;
    }

    QLineEdit:focus, QTextEdit:focus {
        border: 3px solid rgb(153, 195, 245);
        padding: 1px;
    }

    QPushButton {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(242, 242, 242),
            stop: 1 rgb(233, 233, 233));
        font-size: 14px;
        border-top: 1px solid rgb(202, 202, 202);
        border-bottom: 1px solid rgb(159, 159, 159);
        border-left: 1px solid rgb(195, 195, 195);
        border-right: 1px solid rgb(195, 195, 195);
        border-radius: 6px;
        padding: 2px 10px;
    }
    
    QPushButton:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }

    QPushButton:disabled {
        color: gray;
        border-top: 1px solid rgb(222, 222, 222);
        border-bottom: 1px solid rgb(179, 179, 179);
        border-left: 1px solid rgb(215, 215, 215);
        border-right: 1px solid rgb(215, 215, 215);
    }

    QPushButton#blue_button {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QPushButton#blue_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(128, 199, 255),
            stop: 1 rgb(26, 175, 255));
        border-top: 1px solid rgb(96, 182, 255);
        border-bottom: 1px solid rgb(23, 112, 255);
        border-left: 1px solid rgb(57, 147, 255);
        border-right: 1px solid rgb(57, 147, 255);
    }

    QPushButton#blue_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QPushButton#blue_button:disabled {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(200, 200, 200),
            stop: 1 rgb(180, 180, 180));
        border-top: 1px solid rgb(222, 222, 222);
        border-bottom: 1px solid rgb(179, 179, 179);
        border-left: 1px solid rgb(215, 215, 215);
        border-right: 1px solid rgb(215, 215, 215);
    }

    QPushButton#exit_button {
        background: transparent;
        border-image: url(./image/gui/close.png) 0 0 0 0 stretch stretch; 
        border: none;
    }
    QPushButton#changesv_button {
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
        background-color:rgb(255, 69, 58);
    }
        

    QPushButton#exit_button:hover {
        border-image: url(./image/gui/close_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#exit_button:pressed {
        border-image: url(./image/gui/close_pressed.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button {
        background: transparent;
        border-image: url(./image/gui/minimize.png) 0 0 0 0 stretch stretch; 
        border: none;
    }

    QPushButton#minimize_button:hover {
        border-image: url(./image/gui/minimize_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button:pressed {
        border-image: url(./image/gui/minimize_pressed.png) 0 0 0 0 stretch stretch; 
    }
    
    QPushButton#minimize_button:disabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button {
        background: transparent;
        border-image: url(./image/gui/fullscreen.png) 0 0 0 0 stretch stretch; 
        border: none;
    }
    QPushButton#user_button {
        background: transparent;
        border: none;
    }

    QPushButton#fullscreen_button:hover {
        border-image: url(./image/gui/fullscreen_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button:pressed {
        border-image: url(./image/gui/fullscreen_pressed.png) 0 0 0 0 stretch stretch; 
    }
    
    QPushButton#fullscreen_button:disabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#back_button {
        background: url(./image/gui/back.png);
    }

    QPushButton#back_button:disabled {
        background: url(./image/gui/back_disabled.png);
    }

    QPushButton#forward_button {
        background: url(./image/gui/forward.png);
    }
    
    QPushButton#forward_button:disabled {
        background: url(./image/gui/forward_disabled.png);
    }

    QPushButton#add_button {
        background: url(./image/gui/add_button.png)
    }

    QPushButton#search_button {
        background: url(./image/gui/search_button.png)
    }

    QPushButton#settings_button {
        background: url(./image/gui/settings_button.png)
    }

    QPushButton#contacts_button {
        background: url(./image/gui/contacts_button.png)
    }

    QLabel#my_fullname {
        font-size: 17px;
    }

    QWidget#sidebar_button {
        background: rgb(220, 220, 220);
    }

    QPushButton#sidebar_item {
        font-size: 16px;
        background: transparent;
        text-align: left;
        border: none;
        border-radius: 0;
        padding-left: 70px;
    }

    QPushButton#sidebar_item:hover {
        background: rgb(228, 228, 228);
    }

    QComboBox {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(242, 242, 242),
            stop: 1 rgb(233, 233, 233));
        border-top: 1px solid rgb(202, 202, 202);
        border-bottom: 1px solid rgb(159, 159, 159);
        border-left: 1px solid rgb(195, 195, 195);
        border-right: 1px solid rgb(195, 195, 195);
        font-size: 14px;
        border-radius: 6px;
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        padding: 2px 10px;
    }

    QComboBox:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QComboBox:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }

    QComboBox:disabled {
        color: gray;
        border-top: 1px solid rgb(222, 222, 222);
        border-bottom: 1px solid rgb(179, 179, 179);
        border-left: 1px solid rgb(215, 215, 215);
        border-right: 1px solid rgb(215, 215, 215);
    }

    QComboBox:drop-down {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-right: 1px solid rgb(37, 127, 252);
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        width: 15px;
        padding: 0px;
        margin: -1px;
    }

    QComboBox:drop-down:disabled {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(172, 172, 172),
            stop: 1 rgb(123, 123, 123));
        border-top: 1px solid rgb(154, 154, 154);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-right: 1px solid rgb(129, 129, 129);
    }

    QComboBox:down-arrow {
        image: url(./image/gui/combo_box_arrows.png);
    }

    QComboBox QAbstractItemView {
        background: white;
    }

    QListWidget {
        font-size: 18px;
        background: transparent;
        border: none;
        outline: none
    }

    QListWidget::item {
        color: transparent;
        border-bottom: 1px solid rgb(200, 200, 200);
        height: 50px;
        margin-left: 2px;
    }

    QListWidget::item:hover {
        background: rgb(227, 227, 227)
    }

    QListWidget::item::selected {
        background: rgb(220, 220, 220)
    }

    QLabel#listItem_upLabel {
        font-size: 15px
    }

    QLabel#listItem_downLabel {
        font-size: 11px;
        color: gray;
    }

    QScrollBar:vertical {
        background: transparent;
        width: 8px;
        margin: 0px 0px 0px 0px;
    }

    QScrollBar::handle:vertical {
        background: rgb(200, 200, 200);
        border-radius: 4px;
        min-height: 20px;
    }

    QScrollBar::handle:vertical:hover {
        background: rgb(170, 170, 170);
    }

    QScrollBar::handle:vertical:pressed {
        background: rgb(130, 130, 130);
    }    

    QScrollBar::add-line:vertical {
        border: none;
        background: transparent;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical {
        border: none;
        background: transparent;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        border: none;
        width: 3px;
        height: 15px;
        background: transparent;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QWidget#intro_widget {
        background: transparent;
        color: rgb(190, 190, 190);
        border-bottom-right-radius: 5px;
        font-weight: bold;
    }

    QWidget#contact_box {
        background: rgb(220, 220, 220);
        border-bottom-right-radius: 5px;
    }

    QWidget#contact_box QWidget#contact_name_box,
    QWidget#contact_box QWidget#contact_phone_box,
    QWidget#contact_box QWidget#contact_email_box,
    QWidget#contact_box QWidget#contact_sns_box,
    QWidget#contact_box QWidget#contact_address_box,
    QWidget#contact_box QWidget#contact_birthday_box {
        background: rgb(235, 235, 235);
        border-radius: 10px;
    }
    QWidget#result_box {
        background: rgb(229, 229, 234);
        border-radius: 10px;
    }    
    QWidget#chart_container {
        background: rgb(229, 229, 234);
        border-image: url(./7daysChart.png) 0 0 0 0 stretch stretch;
    }
    QWidget#info_box {
        background: rgb(229, 229, 234);
        border-radius: 10px;
    }
    QLabel#info_lb {
        background: rgb(235, 235, 235);
        border-radius: 10px;
    }
    QLabel#info_title {
        font-size: 20px;
        font-family: junegull;
        color: black;
    }
    QLabel#info_text {
        font-size: 15px;
        font-family: Open Sans Light;
        color: #000072;
        font-weight: 300;
    }

    QWidget#contact_box QLabel {
        color: blue;
        font-size: 13px;
    }

    QWidget#contact_box_scroll,
    QWidget#create_contact_box_scroll,
    QWidget#edit_contact_box_scroll {
        background: transparent;
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QLabel {
        color: black;
    }

    QWidget#contact_box QWidget#contact_name_box QLabel:hover {
        color: red;
    }

    QWidget#contact_box QWidget#contact_name_box QLabel#contact_fullname {
        font-size: 19px;
    }

    QWidget#contact_box QWidget#contact_name_box QLabel#contact_nickname {
        font-size: 15px; 
        font-style: italic;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button {
        background: url(./image/gui/phone.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button:hover {
        background: url(./image/gui/phone_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button:pressed {
        background: url(./image/gui/phone_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button:disabled {
        background: url(./image/gui/phone_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button {
        background: url(./image/gui/sms.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button:hover {
        background: url(./image/gui/sms_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button:pressed {
        background: url(./image/gui/sms_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button:disabled {
        background: url(./image/gui/sms_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button {
        background: url(./image/gui/facetime.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button:hover {
        background: url(./image/gui/facetime_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button:pressed {
        background: url(./image/gui/facetime_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button:disabled {
        background: url(./image/gui/facetime_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button {
        background: url(./image/gui/email.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button:hover {
        background: url(./image/gui/email_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button:pressed {
        background: url(./image/gui/email_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button:disabled {
        background: url(./image/gui/email_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button {
        background: url(./image/gui/facebook.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button:hover {
        background: url(./image/gui/facebook_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button:pressed {
        background: url(./image/gui/facebook_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button:disabled {
        background: url(./image/gui/facebook_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button {
        background: url(./image/gui/twitter.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button:hover {
        background: url(./image/gui/twitter_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button:pressed {
        background: url(./image/gui/twitter_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button:disabled {
        background: url(./image/gui/twitter_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button {
        background: url(./image/gui/instagram.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button:hover {
        background: url(./image/gui/instagram_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button:pressed {
        background: url(./image/gui/instagram_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button:disabled {
        background: url(./image/gui/instagram_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button {
        background: url(./image/gui/map.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button:hover {
        background: url(./image/gui/map_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button:pressed {
        background: url(./image/gui/map_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button:disabled {
        background: url(./image/gui/map_disabled.png);
    }
    
    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_edit_button {
        font-size: 12px;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_remove_button {
        color: red;
        font-size: 12px;
        padding: 1px;
    }

    QWidget#contact_box QWidget QLabel:hover {
        color: red;
    }

    QWidget#contact_box QWidget QLabel#label {
        color: gray;
        font-weight: bold;
        font-style: italic;
    }

    QWidget#contact_box QWidget QLabel#label:hover {
        color: blue;
    }


    QWidget#contact_edit_create {
        background: rgb(220, 220, 220);
    }

    QWidget#contact_edit_create QGroupBox {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
    }

    QWidget#contact_edit_create QLabel {
        border: none;
        padding: 2px;
    }

    QWidget#contact_edit_create QGroupBox#edit_profile_picture_box QLabel#edit_picture_label {
        color: white;
        background-color: rgba(0, 0, 0, 0.3);
    }

    QWidget#contact_edit_create QPushButton,
    QWidget#contact_edit_create QLineEdit,
    QWidget#contact_edit_create QTextEdit,
    QWidget#contact_edit_create QComboBox {
        font-size: 12px;
        padding: 0;
    }

    QWidget#contact_edit_create QComboBox {
        font-size: 12px;
        padding: 3px;
    }

    QWidget#contact_edit_create QGroupBox#edit_profile_picture_box QPushButton#edit_profile_picture_button {
        color: white;
        background: transparent;
        border: 1px solid #69bad1;
        border-radius: 2px;
        padding: 2px;
    }

    QWidget#contact_edit_create QGroupBox#edit_profile_picture_box QPushButton#edit_profile_picture_button:hover {
        border-width: 2px;
    }
    
    QLabel#messagebox_boldtext {
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton#messagebox_ok {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QWidget#usersettings_box {
        background: rgb(220, 220, 220);
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
    }

    QWidget#usersettings_box QWidget#settings_subwidget {
        background: rgb(220, 220, 220);
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
    }

    QWidget#usersettings_box QListWidget#settings_list {
        background: rgb(227, 227, 227);
        border-right: 1px solid rgb(200, 200, 200);
    }

    QWidget#usersettings_box QListWidget#settings_list::item {
        margin-left: 2px;
        margin-right: 2px;
    }

    QWidget#usersettings_box QLabel#profile_picture {
        background: rgb(235, 235, 235);
        border: 1px solid rgb(190, 190, 190);
        border-radius: 3px;
        padding: 4px;
    }

    QWidget#usersettings_box QLabel#settings_description,
    QWidget#usersettings_box QWidget#field_container {
        background: rgb(235, 235, 235);
        padding: 10px;
        border-radius: 15px;
        padding: 10px 20px;
    }

    QWidget#usersettings_box QPushButton#save_button {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QWidget#usersettings_box QPushButton#save_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(128, 199, 255),
            stop: 1 rgb(26, 175, 255));
        border-top: 1px solid rgb(96, 182, 255);
        border-bottom: 1px solid rgb(23, 112, 255);
        border-left: 1px solid rgb(57, 147, 255);
        border-right: 1px solid rgb(57, 147, 255);
    }

    QWidget#usersettings_box QPushButton#save_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QWidget#usersettings_box QPushButton#save_button:disabled {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(200, 200, 200),
            stop: 1 rgb(180, 180, 180));
        border-top: 1px solid rgb(222, 222, 222);
        border-bottom: 1px solid rgb(179, 179, 179);
        border-left: 1px solid rgb(215, 215, 215);
        border-right: 1px solid rgb(215, 215, 215);
    }

    QWidget#usersettings_box QLabel#field_label {
        color: gray;
        font-weight: bold;
        font-style: italic;
    }

    QWidget#usersettings_box QPushButton#theme_selection {
        background: transparent;
        border: 3px solid rgb(0, 131, 255);
        border-radius: 7px;
    }

    QWidget#usersettings_box QLabel#theme_label {
        color: rgb(120, 120, 120);
        font-weight: bold;
    }

    QWidget#usersettings_box QLabel#username {
        color: gray;
        font-style: italic;
    }

    QWidget#usersettings_box QWidget#language_options {
        background: rgb(220, 220, 220);
        border-radius: 15px;
    }

    QWidget#usersettings_box QPushButton#language_item {
        background: transparent;
        color: rgb(130, 130, 130);
        font-size: 13px;
        font-weight: bold;
        border: none;
        text-align: center;
    }

    QWidget#usersettings_box QPushButton#language_selection {
        font-size: 13px;
        font-weight: bold;
        border-radius: 15px;
        padding: 1px;
    }

    QWidget#image_crop_box {
        background: white;
        border: 1px solid rgb(190, 190, 190);
        padding: 5px;
        border-radius: 3px;
    }

    QWidget#crop_image_rect {
        background: rgba(180, 180, 255, 0.3);
        border: 1px solid rgb(180, 180, 255);
    }

    QWidget#crop_image_resize_point {
        background: rgb(180, 180, 255);
    }
"""

basegui_darktheme = """
    QWidget {
        color: rgb(220, 220, 220);
        font-size: 14px;
        font-family: Arial;
    }

    QWidget#container {
        background: rgba(50, 50, 50, 1);
        border-radius: 5px;
        border: 1px solid rgb(91, 91, 91);
    }
    QWidget#background {
        background: rgba(50, 50, 50, 1);
        border-radius: 5px;
        border: 1px solid rgb(91, 91, 91);
    }

    QWidget#messagebox_container {
        background: rgba(50, 50, 50, 1);
        border-radius: 5px;
        border: 1px solid rgb(91, 91, 91);
        border-bottom-left-radius: 10px;
    }
    QWidget#main_container {
        background: rgb(235, 235, 235);
        border-radius: 5px;
        border: 1px solid rgb(91, 91, 91);
        border-bottom-left-radius: 7px;
    }
    
    QWidget#titlebar {
        font-size: 16px;
        color: rgb(205, 205, 205);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(67, 67, 67),
            stop: 1 rgb(56, 56, 56));
        border: 1px solid rgb(91, 91, 91);
        border-top: 1px solid rgb(121, 121, 121);
        border-bottom: 1px solid rgb(35, 35, 35);
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
    }

    QWidget#profile_popup {
        background: rgba(62, 62, 62, 0.9);
        border: 1px solid rgb(90, 90, 90);
        border-top: none;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
    }

    QWidget#profile_popup QLabel#profile_fullname {
        color: rgb(240, 240, 240);
        font-size: 16px;
    }

    QWidget#profile_popup QLabel#profile_username {
        color: gray;
        font-size: 14px;
        font-style: italic;
    }

    QWidget#profile_popup QPushButton {
        font-size: 12px;
    }

    QWidget#sidebar {
        background: rgb(42, 42, 42);
        border-right: 1px solid rgb(65, 65, 65);
        border-bottom-left-radius: 7px;
    }

    QWidget#sidebar QLineEdit#searchbox {
        border: none;
        font-size: 15px;
        background: rgb(58, 58, 58);
        padding-left: 5px;
        border-radius: none;
    }
    
    QWidget#sidebar QLineEdit#searchbox:focus {
        background: rgb(78, 78, 78);
        border: none;
    }

    QWidget#sidebar QLineEdit#searchbox QPushButton#search_clear {
        background: url(./image/gui/clear.png);
        border: none;
    }

    QLineEdit, QTextEdit {
        color: rgb(220, 220, 220);
        font-size: 13px;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(30, 30, 30),
            stop: 0.2 rgb(40, 40, 40));
        font-size: 14px;
        border: 1px solid rgb(64, 64, 64);
        border-bottom: rgb(87, 87, 87);
        border-radius: 6px;
        padding: 3px;
    }

    QLineEdit:focus, QTextEdit:focus {
        border: 3px solid rgb(29, 108, 150);
        padding: 1px;
    }

    QPushButton {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(109, 109, 109),
            stop: 1 rgb(102, 102, 102));
        font-size: 14px;
        border: 1px solid rgb(102, 102, 102);
        border-top: 1px solid rgb(137, 137, 137);
        border-radius: 6px;
        padding: 2px 10px;
    }
    
    QPushButton:hover {
        background: rgb(126, 126, 126);
        border: 1px solid rgb(126, 126, 126);
        border-top: 1px solid rgb(157, 157, 157);
    }
    
    QPushButton:pressed {
        background: rgb(106, 106, 106);
        border: 1px solid rgb(106, 106, 106);
        border-top: 1px solid rgb(137, 137, 137);
    }

    QPushButton:disabled {
        color: rgb(120, 120, 120);
        background: rgb(76, 76, 76);
        border: 1px solid rgb(76, 76, 76);
        border-top: 1px solid rgb(97, 97, 97);
    }

    QPushButton#blue_button {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(25, 103, 229),
            stop: 1 rgb(20, 93, 205));
        border-top: 1px solid rgb(88, 147, 238);
        border-bottom: 1px solid rgb(32, 74, 145);
        border-left: 1px solid rgb(26, 92, 194);
        border-right: 1px solid rgb(26, 92, 194);
    }

    QPushButton#blue_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(45, 123, 249),
            stop: 1 rgb(40, 113, 225));
        border-top: 1px solid rgb(108, 167, 255);
        border-bottom: 1px solid rgb(52, 94, 165);
        border-left: 1px solid rgb(46, 112, 214);
        border-right: 1px solid rgb(46, 112, 214);
    }

    QPushButton#blue_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(25, 103, 229),
            stop: 1 rgb(20, 93, 205));
        border-top: 1px solid rgb(88, 147, 238);
        border-bottom: 1px solid rgb(32, 74, 145);
        border-left: 1px solid rgb(26, 92, 194);
        border-right: 1px solid rgb(26, 92, 194);
    }

    QPushButton#blue_button:disabled {
        color: gray;
        background: rgb(76, 76, 76);
        border: 1px solid rgb(76, 76, 76);
        border-top: 1px solid rgb(97, 97, 97);
    }

    QPushButton#exit_button {
        background: transparent;
        border-image: url(./image/gui/close.png) 0 0 0 0 stretch stretch; 
        border: none;
    }

    QPushButton#exit_button:hover {
        border-image: url(./image/gui/close_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#exit_button:pressed {
        border-image: url(./image/gui/close_pressed.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button {
        background: transparent;
        border-image: url(./image/gui/minimize.png) 0 0 0 0 stretch stretch; 
        border: none;
    }

    QPushButton#minimize_button:hover {
        border-image: url(./image/gui/minimize_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#minimize_button:pressed {
        border-image: url(./image/gui/minimize_pressed.png) 0 0 0 0 stretch stretch; 
    }
    
    QPushButton#minimize_button:disabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button {
        background: transparent;
        border-image: url(./image/gui/fullscreen.png) 0 0 0 0 stretch stretch; 
        border: none;
    }

    QPushButton#fullscreen_button:hover {
        border-image: url(./image/gui/fullscreen_hover.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#fullscreen_button:pressed {
        border-image: url(./image/gui/fullscreen_pressed.png) 0 0 0 0 stretch stretch; 
    }
    
    QPushButton#fullscreen_button:disabled {
        border-image: url(./image/gui/disabled.png) 0 0 0 0 stretch stretch; 
    }

    QPushButton#back_button {
        background: url(./image/gui/back_dark.png);
    }

    QPushButton#back_button:hover {
        background: url(./image/gui/back_dark_hover.png);
    }

    QPushButton#back_button:pressed {
        background: url(./image/gui/back_dark.png);
    }

    QPushButton#back_button:disabled {
        background: url(./image/gui/back_dark_disabled.png);
    }

    QPushButton#forward_button {
        background: url(./image/gui/forward_dark.png);
    }

    QPushButton#forward_button:hover {
        background: url(./image/gui/forward_dark_hover.png);
    }

    QPushButton#forward_button:pressed {
        background: url(./image/gui/forward_dark.png);
    }
    
    QPushButton#forward_button:disabled {
        background: url(./image/gui/forward_dark_disabled.png);
    }

    QPushButton#add_button {
        background: url(./image/gui/add_button_dark.png)
    }

    QPushButton#add_button:hover {
        background: url(./image/gui/add_button_dark_hover.png)
    }

    QPushButton#add_button:pressed {
        background: url(./image/gui/add_button_dark.png)
    }

    QPushButton#search_button {
        background: url(./image/gui/search_button_dark.png)
    }

    QPushButton#search_button:hover {
        background: url(./image/gui/search_button_dark_hover.png)
    }

    QPushButton#search_button:pressed {
        background: url(./image/gui/search_button_dark.png)
    }

    QPushButton#settings_button {
        background: url(./image/gui/settings_button.png)
    }

    QPushButton#contacts_button {
        background: url(./image/gui/contacts_button.png)
    }

    QLabel#my_fullname {
        font-size: 17px;
    }

    QComboBox {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(137, 137, 137),
            stop: 0.05 rgb(109, 109, 109),
            stop: 1 rgb(102, 102, 102));
        font-size: 14px;
        border: none;
        border-radius: 6px;
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        padding: 2px 10px;
    }

    QComboBox:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(157, 157, 157),
            stop: 0.05 rgb(126, 126, 126),
            stop: 1 rgb(126, 126, 126));
    }

    QComboBox:disabled {
        color: rgb(120, 120, 120);
        background: rgb(76, 76, 76);
        border: 1px solid rgb(76, 76, 76);
        border-top: 1px solid rgb(97, 97, 97);
    }

    QComboBox:drop-down {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgba(25, 103, 229, 0.8),
            stop: 1 rgba(20, 93, 205, 0.8));
        border-top: 1px solid rgb(88, 147, 238);
        border-right: 1px solid rgb(26, 92, 194);
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        width: 15px;
        padding: 0px;
    }

    QComboBox:drop-down:disabled {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(109, 109, 109),
            stop: 0.05 rgb(92, 92, 92),
            stop: 1 rgb(84, 84, 84));
        border: none;
    }

    QComboBox:down-arrow {
        image: url(./image/gui/combo_box_arrows.png);
    }

    QComboBox:down-arrow:disabled {
        image: url(./image/gui/combo_box_arrows_disabled.png);
    }

    QComboBox QAbstractItemView {
        background: rgb(50, 50, 50);
    }

    QWidget#sidebar_button {
        background: rgb(220, 220, 220);
    }

    QPushButton#sidebar_item {
        font-size: 16px;
        background: transparent;
        text-align: left;
        border: none;
        border-radius: 0;
        padding-left: 70px;
    }

    QPushButton#sidebar_item:hover {
        background: rgb(51, 51, 51);
    }

    QListWidget {
        font-size: 18px;
        background: transparent;
        border: none;
        outline: none
    }

    QListWidget::item {
        color: transparent;
        border-bottom: 1px solid rgb(70, 70, 70);
        height: 50px;
        margin-left: 2px;
    }

    QListWidget::item:hover {
        background: rgb(51, 51, 51)
    }

    QListWidget::item::selected {
        background: rgb(58, 58, 58)
    }

    QLabel#listItem_upLabel {
        font-size: 15px
    }

    QLabel#listItem_downLabel {
        font-size: 11px;
        color: gray;
    }

    QScrollBar:vertical {
        background: transparent;
        width: 8px;
        margin: 0px 0px 0px 0px;
    }

    QScrollBar::handle:vertical {
        background: rgb(70, 70, 70);
        border-radius: 4px;
        min-height: 20px;
    }

    QScrollBar::handle:vertical:hover {
        background: rgb(100, 100, 100);
    }

    QScrollBar::handle:vertical:pressed {
        background: rgb(70, 70, 70);
    }    

    QScrollBar::add-line:vertical {
        border: none;
        background: transparent;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical {
        border: none;
        background: transparent;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        border: none;
        width: 3px;
        height: 15px;
        background: transparent;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QWidget#contact_box {
        background: rgba(50, 50, 50, 1);
        border-bottom-right-radius: 4px;
    }

    QWidget#contact_box_scroll {
        background: transparent;
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box,
    QWidget#contact_box QWidget#contact_phone_box,
    QWidget#contact_box QWidget#contact_email_box,
    QWidget#contact_box QWidget#contact_sns_box,
    QWidget#contact_box QWidget#contact_address_box,
    QWidget#contact_box QWidget#contact_note_box,
    QWidget#contact_box QWidget#contact_birthday_box {
        background: rgb(63, 63, 63);
        border-radius: 10px;
    }

    QWidget#contact_box QLabel {
        color: rgb(150, 200, 255);
        font-size: 19px;
    }
    

    QWidget#contact_box QWidget#contact_name_box QLabel {
        color: rgb(200, 200, 200);
    }

    QWidget#contact_box QWidget#contact_name_box QLabel:hover {
        color: red;
    }

    QWidget#contact_box QWidget#contact_name_box QLabel#contact_fullname {
        font-size: 19px;
    }

    QWidget#contact_box QWidget#contact_name_box QLabel#contact_nickname {
        font-size: 15px; 
        font-style: italic;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button {
        background: url(./image/gui/phone.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button:hover {
        background: url(./image/gui/phone_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button:pressed {
        background: url(./image/gui/phone_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_phone_button:disabled {
        background: url(./image/gui/phone_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button {
        background: url(./image/gui/sms.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button:hover {
        background: url(./image/gui/sms_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button:pressed {
        background: url(./image/gui/sms_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_message_button:disabled {
        background: url(./image/gui/sms_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button {
        background: url(./image/gui/facetime.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button:hover {
        background: url(./image/gui/facetime_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button:pressed {
        background: url(./image/gui/facetime_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facetime_button:disabled {
        background: url(./image/gui/facetime_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button {
        background: url(./image/gui/email.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button:hover {
        background: url(./image/gui/email_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button:pressed {
        background: url(./image/gui/email_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_email_button:disabled {
        background: url(./image/gui/email_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button {
        background: url(./image/gui/facebook.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button:hover {
        background: url(./image/gui/facebook_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button:pressed {
        background: url(./image/gui/facebook_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_facebook_button:disabled {
        background: url(./image/gui/facebook_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button {
        background: url(./image/gui/twitter.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button:hover {
        background: url(./image/gui/twitter_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button:pressed {
        background: url(./image/gui/twitter_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_twitter_button:disabled {
        background: url(./image/gui/twitter_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button {
        background: url(./image/gui/instagram.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button:hover {
        background: url(./image/gui/instagram_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button:pressed {
        background: url(./image/gui/instagram_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_instagram_button:disabled {
        background: url(./image/gui/instagram_disabled.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button {
        background: url(./image/gui/map.png);
        border: none;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button:hover {
        background: url(./image/gui/map_hover.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button:pressed {
        background: url(./image/gui/map_pressed.png);
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_map_button:disabled {
        background: url(./image/gui/map_disabled.png);
    }
    
    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_edit_button {
        font-size: 12px;
    }

    QWidget#contact_box QWidget#contact_name_box QPushButton#contact_remove_button {
        color: red;
        font-size: 12px;
        padding: 1px;
    }

    QWidget#contact_box QWidget QLabel:hover {
        color: red;
    }

    QWidget#contact_box QWidget QLabel#label {
        color: gray;
        font-weight: bold;
        font-style: italic;
    }

    QWidget#contact_box QWidget QLabel#label:hover {
        color: rgb(150, 200, 255);
    }


    QWidget#contact_edit_create {
        background: rgba(50, 50, 50, 1);
        border-bottom-right-radius: 4px;
    }

    QWidget#contact_edit_create QGroupBox {
        background: rgb(63, 63, 63);
        border-radius: 10px;
    }

    QWidget#contact_edit_create QLabel {
        border: none;
        padding: 2px;
    }

    QWidget#contact_edit_create QGroupBox#edit_profile_picture_box QLabel#edit_picture_label {
        color: white;
        background-color: rgba(0, 0, 0, 0.3);
    }

    QWidget#contact_edit_create QPushButton,
    QWidget#contact_edit_create QLineEdit,
    QWidget#contact_edit_create QTextEdit,
    QWidget#contact_edit_create QComboBox {
        font-size: 12px;
        padding: 0;
    }

    QWidget#contact_edit_create QComboBox {
        font-size: 12px;
        padding: 3px;
    }

    QWidget#contact_edit_create QGroupBox#edit_profile_picture_box QPushButton#edit_profile_picture_button {
        color: white;
        background: transparent;
        border: 1px solid #69bad1;
        border-radius: 2px;
        padding: 2px;
    }

    QWidget#contact_edit_create QGroupBox#edit_profile_picture_box QPushButton#edit_profile_picture_button:hover {
        border-width: 2px;
    }
    
    QLabel#messagebox_boldtext {
        font-size: 14px;
        font-weight: bold;
    }

    QWidget#usersettings_box {
        background: rgba(50, 50, 50, 1);
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
    }

    QWidget#usersettings_box QWidget#settings_subwidget {
        background: rgba(50, 50, 50, 1);
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
    }

    QWidget#usersettings_box QListWidget#settings_list {
        background: rgb(46, 46, 46);
        border-right: 1px solid rgb(65, 65, 65);
    }

    QWidget#usersettings_box QListWidget#settings_list::item {
        margin-left: 2px;
        margin-right: 2px;
    }

    QWidget#usersettings_box QListWidget#settings_list::item:hover {
        background: rgb(51, 51, 51);
    }

    QWidget#usersettings_box QListWidget#settings_list::item:selected {
        background: rgb(65, 65, 65);
    }

    QWidget#usersettings_box QLabel#profile_picture {
        background: rgb(90, 90, 90);
        border: 1px solid rgb(110, 110, 110);
        border-radius: 3px;
        padding: 4px;
    }

    QWidget#usersettings_box QLabel#settings_description,
    QWidget#usersettings_box QWidget#field_container {
        color: rgb(200, 200, 200);
        background: rgb(63, 63, 63);
        padding: 10px;
        border-radius: 15px;
        padding: 10px 20px;
    }

    QWidget#usersettings_box QPushButton#save_button {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(25, 103, 229),
            stop: 1 rgb(20, 93, 205));
        border-top: 1px solid rgb(88, 147, 238);
        border-bottom: 1px solid rgb(32, 74, 145);
        border-left: 1px solid rgb(26, 92, 194);
        border-right: 1px solid rgb(26, 92, 194);
    }

    QWidget#usersettings_box QPushButton#save_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(45, 123, 249),
            stop: 1 rgb(40, 113, 225));
        border-top: 1px solid rgb(108, 167, 255);
        border-bottom: 1px solid rgb(52, 94, 165);
        border-left: 1px solid rgb(46, 112, 214);
        border-right: 1px solid rgb(46, 112, 214);
    }

    QWidget#usersettings_box QPushButton#save_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(25, 103, 229),
            stop: 1 rgb(20, 93, 205));
        border-top: 1px solid rgb(88, 147, 238);
        border-bottom: 1px solid rgb(32, 74, 145);
        border-left: 1px solid rgb(26, 92, 194);
        border-right: 1px solid rgb(26, 92, 194);
    }

    QWidget#usersettings_box QPushButton#save_button:disabled {
        color: gray;
        background: rgb(76, 76, 76);
        border: 1px solid rgb(76, 76, 76);
        border-top: 1px solid rgb(97, 97, 97);
    }

    QWidget#usersettings_box QLabel#field_label {
        color: gray;
        font-weight: bold;
        font-style: italic;
    }

    QWidget#usersettings_box QPushButton#theme_selection {
        background: transparent;
        border: 3px solid rgb(0, 131, 255);
        border-radius: 7px;
    }

    QWidget#usersettings_box QLabel#theme_label {
        color: rgb(120, 120, 120);
        font-weight: bold;
    }

    QWidget#usersettings_box QLabel#username {
        color: gray;
        font-style: italic;
    }

    QWidget#usersettings_box QWidget#language_options {
        background: rgb(50, 50, 50);
        border-radius: 15px;
    }

    QWidget#usersettings_box QPushButton#language_item {
        background: transparent;
        color: rgb(130, 130, 130);
        font-size: 13px;
        font-weight: bold;
        border: none;
        text-align: center;
    }

    QWidget#usersettings_box QPushButton#language_selection {
        font-size: 13px;
        font-weight: bold;
        border-radius: 15px;
        padding: 1px;
    }
    
    QWidget#image_crop_box {
        background: white;
        border: 1px solid rgb(190, 190, 190);
        padding: 5px;
        border-radius: 3px;
    }

    QWidget#crop_image_rect {
        background: rgba(180, 180, 255, 0.3);
        border: 1px solid rgb(180, 180, 255);
    }

    QWidget#crop_image_resize_point {
        background: rgb(180, 180, 255);
    }
"""
