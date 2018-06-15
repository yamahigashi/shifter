import mgear.core.pyqt as gqt
from mgear.vendor.Qt import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 809)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.L_color_fk_label = QtWidgets.QLabel(self.groupBox_5)
        self.L_color_fk_label.setObjectName("L_color_fk_label")
        self.horizontalLayout_3.addWidget(self.L_color_fk_label)
        self.L_color_fk_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_color_fk_spinBox.sizePolicy().hasHeightForWidth())
        self.L_color_fk_spinBox.setSizePolicy(sizePolicy)
        self.L_color_fk_spinBox.setMaximum(31)
        self.L_color_fk_spinBox.setObjectName("L_color_fk_spinBox")
        self.horizontalLayout_3.addWidget(self.L_color_fk_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.L_color_fk_label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.L_color_fk_label_5.setObjectName("L_color_fk_label_5")
        self.horizontalLayout_7.addWidget(self.L_color_fk_label_5)
        self.C_color_fk_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_color_fk_spinBox.sizePolicy().hasHeightForWidth())
        self.C_color_fk_spinBox.setSizePolicy(sizePolicy)
        self.C_color_fk_spinBox.setMaximum(31)
        self.C_color_fk_spinBox.setObjectName("C_color_fk_spinBox")
        self.horizontalLayout_7.addWidget(self.C_color_fk_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.L_color_fk_label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.L_color_fk_label_3.setObjectName("L_color_fk_label_3")
        self.horizontalLayout_5.addWidget(self.L_color_fk_label_3)
        self.R_color_fk_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_color_fk_spinBox.sizePolicy().hasHeightForWidth())
        self.R_color_fk_spinBox.setSizePolicy(sizePolicy)
        self.R_color_fk_spinBox.setMaximum(31)
        self.R_color_fk_spinBox.setObjectName("R_color_fk_spinBox")
        self.horizontalLayout_5.addWidget(self.R_color_fk_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.L_color_fk_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.L_color_fk_label_2.setObjectName("L_color_fk_label_2")
        self.horizontalLayout_4.addWidget(self.L_color_fk_label_2)
        self.L_color_ik_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_color_ik_spinBox.sizePolicy().hasHeightForWidth())
        self.L_color_ik_spinBox.setSizePolicy(sizePolicy)
        self.L_color_ik_spinBox.setMaximum(31)
        self.L_color_ik_spinBox.setObjectName("L_color_ik_spinBox")
        self.horizontalLayout_4.addWidget(self.L_color_ik_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.L_color_fk_label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.L_color_fk_label_6.setObjectName("L_color_fk_label_6")
        self.horizontalLayout_8.addWidget(self.L_color_fk_label_6)
        self.C_color_ik_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_color_ik_spinBox.sizePolicy().hasHeightForWidth())
        self.C_color_ik_spinBox.setSizePolicy(sizePolicy)
        self.C_color_ik_spinBox.setMaximum(31)
        self.C_color_ik_spinBox.setObjectName("C_color_ik_spinBox")
        self.horizontalLayout_8.addWidget(self.C_color_ik_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.L_color_fk_label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.L_color_fk_label_4.setObjectName("L_color_fk_label_4")
        self.horizontalLayout_6.addWidget(self.L_color_fk_label_4)
        self.R_color_ik_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_color_ik_spinBox.sizePolicy().hasHeightForWidth())
        self.R_color_ik_spinBox.setSizePolicy(sizePolicy)
        self.R_color_ik_spinBox.setMaximum(31)
        self.R_color_ik_spinBox.setObjectName("R_color_ik_spinBox")
        self.horizontalLayout_6.addWidget(self.R_color_ik_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 6, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.rigName_label = QtWidgets.QLabel(self.groupBox)
        self.rigName_label.setObjectName("rigName_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rigName_label)
        self.rigName_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.rigName_lineEdit.setObjectName("rigName_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rigName_lineEdit)
        self.mode_label = QtWidgets.QLabel(self.groupBox)
        self.mode_label.setObjectName("mode_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mode_label)
        self.mode_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mode_comboBox)
        self.step_label = QtWidgets.QLabel(self.groupBox)
        self.step_label.setObjectName("step_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.step_label)
        self.step_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.step_comboBox.setObjectName("step_comboBox")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.step_comboBox)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.importSkin_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.importSkin_checkBox.setObjectName("importSkin_checkBox")
        self.verticalLayout.addWidget(self.importSkin_checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skin_label = QtWidgets.QLabel(self.groupBox_2)
        self.skin_label.setObjectName("skin_label")
        self.horizontalLayout.addWidget(self.skin_label)
        self.skin_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.skin_lineEdit.setObjectName("skin_lineEdit")
        self.horizontalLayout.addWidget(self.skin_lineEdit)
        self.loadSkinPath_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.loadSkinPath_pushButton.setObjectName("loadSkinPath_pushButton")
        self.horizontalLayout.addWidget(self.loadSkinPath_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rigTabs_label = QtWidgets.QLabel(self.groupBox_4)
        self.rigTabs_label.setObjectName("rigTabs_label")
        self.verticalLayout_3.addWidget(self.rigTabs_label)
        self.rigTabs_listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.rigTabs_listWidget.setDragDropOverwriteMode(True)
        self.rigTabs_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.rigTabs_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.rigTabs_listWidget.setAlternatingRowColors(True)
        self.rigTabs_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rigTabs_listWidget.setSelectionRectVisible(False)
        self.rigTabs_listWidget.setObjectName("rigTabs_listWidget")
        self.verticalLayout_3.addWidget(self.rigTabs_listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.addTab_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.addTab_pushButton.setObjectName("addTab_pushButton")
        self.verticalLayout_4.addWidget(self.addTab_pushButton)
        self.removeTab_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeTab_pushButton.sizePolicy().hasHeightForWidth())
        self.removeTab_pushButton.setSizePolicy(sizePolicy)
        self.removeTab_pushButton.setObjectName("removeTab_pushButton")
        self.verticalLayout_4.addWidget(self.removeTab_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.available_label = QtWidgets.QLabel(self.groupBox_4)
        self.available_label.setObjectName("available_label")
        self.verticalLayout_2.addWidget(self.available_label)
        self.available_listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.available_listWidget.setDragDropOverwriteMode(True)
        self.available_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.available_listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.available_listWidget.setAlternatingRowColors(True)
        self.available_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.available_listWidget.setSelectionRectVisible(False)
        self.available_listWidget.setObjectName("available_listWidget")
        self.verticalLayout_2.addWidget(self.available_listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 5, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.jointRig_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.jointRig_checkBox.setObjectName("jointRig_checkBox")
        self.gridLayout_5.addWidget(self.jointRig_checkBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.proxyChannels_checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.proxyChannels_checkBox.setObjectName("proxyChannels_checkBox")
        self.gridLayout_8.addWidget(self.proxyChannels_checkBox, 0, 0, 1, 1)
        self.classicChannelNames_checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.classicChannelNames_checkBox.setObjectName("classicChannelNames_checkBox")
        self.gridLayout_8.addWidget(self.classicChannelNames_checkBox, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.worldCtl_checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.worldCtl_checkBox.setObjectName("worldCtl_checkBox")
        self.gridLayout_9.addWidget(self.worldCtl_checkBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.groupBox_5.setTitle(gqt.fakeTranslate("Form", "Color Settings", None, -1))
        self.label.setText(gqt.fakeTranslate("Form", "Left", None, -1))
        self.label_2.setText(gqt.fakeTranslate("Form", "Center", None, -1))
        self.label_3.setText(gqt.fakeTranslate("Form", "Right", None, -1))
        self.L_color_fk_label.setText(gqt.fakeTranslate("Form", "FK", None, -1))
        self.L_color_fk_label_5.setText(gqt.fakeTranslate("Form", "FK", None, -1))
        self.L_color_fk_label_3.setText(gqt.fakeTranslate("Form", "FK", None, -1))
        self.L_color_fk_label_2.setText(gqt.fakeTranslate("Form", "IK", None, -1))
        self.L_color_fk_label_6.setText(gqt.fakeTranslate("Form", "IK", None, -1))
        self.L_color_fk_label_4.setText(gqt.fakeTranslate("Form", " IK", None, -1))
        self.groupBox.setTitle(gqt.fakeTranslate("Form", "Rig Settings", None, -1))
        self.rigName_label.setText(gqt.fakeTranslate("Form", "Rig Name", None, -1))
        self.mode_label.setText(gqt.fakeTranslate("Form", "Debug Mode", None, -1))
        self.mode_comboBox.setItemText(0, gqt.fakeTranslate("Form", "Final", None, -1))
        self.mode_comboBox.setItemText(1, gqt.fakeTranslate("Form", "WIP", None, -1))
        self.step_label.setText(gqt.fakeTranslate("Form", "Guide Build Steps:", None, -1))
        self.step_comboBox.setItemText(0, gqt.fakeTranslate("Form", "All Steps", None, -1))
        self.step_comboBox.setItemText(1, gqt.fakeTranslate("Form", "Objects", None, -1))
        self.step_comboBox.setItemText(2, gqt.fakeTranslate("Form", "Attributes", None, -1))
        self.step_comboBox.setItemText(3, gqt.fakeTranslate("Form", "Operators", None, -1))
        self.step_comboBox.setItemText(4, gqt.fakeTranslate("Form", "Connect", None, -1))
        self.step_comboBox.setItemText(5, gqt.fakeTranslate("Form", "Joints", None, -1))
        self.step_comboBox.setItemText(6, gqt.fakeTranslate("Form", "Finalize", None, -1))
        self.groupBox_2.setTitle(gqt.fakeTranslate("Form", "Skinning Settings", None, -1))
        self.importSkin_checkBox.setText(gqt.fakeTranslate("Form", "Import Skin", None, -1))
        self.skin_label.setText(gqt.fakeTranslate("Form", "Skin Path", None, -1))
        self.loadSkinPath_pushButton.setText(gqt.fakeTranslate("Form", "Load Path", None, -1))
        self.groupBox_4.setTitle(gqt.fakeTranslate("Form", "Synoptic Settings", None, -1))
        self.rigTabs_label.setText(gqt.fakeTranslate("Form", "Rig Tabs", None, -1))
        self.addTab_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.removeTab_pushButton.setText(gqt.fakeTranslate("Form", ">>", None, -1))
        self.available_label.setText(gqt.fakeTranslate("Form", "Available Tabs", None, -1))
        self.groupBox_3.setTitle(gqt.fakeTranslate("Form", "Joint Settings", None, -1))
        self.jointRig_checkBox.setText(gqt.fakeTranslate("Form", "Separated Joint Structure", None, -1))
        self.groupBox_6.setTitle(gqt.fakeTranslate("Form", "Animation Channels Settings", None, -1))
        self.proxyChannels_checkBox.setText(gqt.fakeTranslate("Form", "Add Internal Proxy Channels", None, -1))
        self.classicChannelNames_checkBox.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>If this option is checked. The channel name will have unique full name. </p><p align=\"center\"><span style=\" font-weight:600;\">i.e: &quot;arm_L0_blend&quot;</span><br/></p><p>If the option is unchecked. The channel will use the simple name. </p><p align=\"center\"><span style=\" font-weight:600;\">i.e: &quot;arm_blend&quot;</span><br/></p><p><span style=\" font-weight:600;\">NOTE</span>: With the option unchecked. If the channel host (uiHost) have 2 or more componets of the same type. The connection will be shared amoung all the componets with the same name channel. </p><p><span style=\" font-weight:600;\">i.e:</span> If we have 2 arms, the channels will be shared for both arms. To avoid this behaviour with the unchecked option, please use a unique channel host for each component.</p></body></html>", None, -1))
        self.classicChannelNames_checkBox.setText(gqt.fakeTranslate("Form", "Use Classic Channel Names (All channels will have unique names.)", None, -1))
        self.groupBox_7.setTitle(gqt.fakeTranslate("Form", "Base Rig Control", None, -1))
        self.worldCtl_checkBox.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>Shifter creates by default a Base control called &quot;<span style=\" font-weight:600;\">global_C0_ctl</span>&quot;. </p><p>Since this control is not accesible from any guide locator. Is not possible to add it as a space reference.</p><p>If this option is active, The base control will be named &quot;<span style=\" font-weight:600;\">world_ctl</span>&quot; and we can add &quot;<span style=\" font-weight:600;\">global_C0_ctl</span>&quot; as a regular &quot;Control_01&quot; component. </p><p>This way we can use it as space reference.</p><p>The biped guide template is configured with this structure.</p></body></html>", None, -1))
        self.worldCtl_checkBox.setText(gqt.fakeTranslate("Form", "Use World Ctl", None, -1))
