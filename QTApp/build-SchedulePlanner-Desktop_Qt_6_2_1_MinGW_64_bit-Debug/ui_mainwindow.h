/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSave_Schedule;
    QAction *actionLoad_Schedule;
    QAction *actionUndo;
    QAction *actionRedo;
    QAction *actionAbout;
    QAction *actionNewClass;
    QAction *actionNewClassSearch;
    QWidget *centralwidget;
    QFrame *HoldingFrame;
    QHBoxLayout *horizontalLayout;
    QFrame *frame;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuEdit;
    QMenu *menuAbout;
    QStatusBar *statusbar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1570, 990);
        actionSave_Schedule = new QAction(MainWindow);
        actionSave_Schedule->setObjectName(QString::fromUtf8("actionSave_Schedule"));
        actionLoad_Schedule = new QAction(MainWindow);
        actionLoad_Schedule->setObjectName(QString::fromUtf8("actionLoad_Schedule"));
        actionUndo = new QAction(MainWindow);
        actionUndo->setObjectName(QString::fromUtf8("actionUndo"));
        actionRedo = new QAction(MainWindow);
        actionRedo->setObjectName(QString::fromUtf8("actionRedo"));
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QString::fromUtf8("actionAbout"));
        actionNewClass = new QAction(MainWindow);
        actionNewClass->setObjectName(QString::fromUtf8("actionNewClass"));
        actionNewClassSearch = new QAction(MainWindow);
        actionNewClassSearch->setObjectName(QString::fromUtf8("actionNewClassSearch"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        HoldingFrame = new QFrame(centralwidget);
        HoldingFrame->setObjectName(QString::fromUtf8("HoldingFrame"));
        HoldingFrame->setGeometry(QRect(300, 580, 1021, 251));
        horizontalLayout = new QHBoxLayout(HoldingFrame);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        frame = new QFrame(centralwidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(560, 270, 161, 111));
        frame->setStyleSheet(QString::fromUtf8("QFrame{\n"
"background:black;\n"
"}"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1570, 21));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        menuEdit = new QMenu(menubar);
        menuEdit->setObjectName(QString::fromUtf8("menuEdit"));
        menuAbout = new QMenu(menubar);
        menuAbout->setObjectName(QString::fromUtf8("menuAbout"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, toolBar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuEdit->menuAction());
        menubar->addAction(menuAbout->menuAction());
        menuFile->addSeparator();
        menuFile->addAction(actionSave_Schedule);
        menuFile->addAction(actionLoad_Schedule);
        menuEdit->addAction(actionUndo);
        menuEdit->addAction(actionRedo);
        menuAbout->addAction(actionAbout);
        toolBar->addAction(actionNewClass);
        toolBar->addAction(actionNewClassSearch);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSave_Schedule->setText(QCoreApplication::translate("MainWindow", "Save Schedule", nullptr));
        actionLoad_Schedule->setText(QCoreApplication::translate("MainWindow", "Load Schedule", nullptr));
        actionUndo->setText(QCoreApplication::translate("MainWindow", "Undo", nullptr));
        actionRedo->setText(QCoreApplication::translate("MainWindow", "Redo", nullptr));
        actionAbout->setText(QCoreApplication::translate("MainWindow", "About", nullptr));
        actionNewClass->setText(QCoreApplication::translate("MainWindow", "NewClass", nullptr));
        actionNewClassSearch->setText(QCoreApplication::translate("MainWindow", "NewClassSearch", nullptr));
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
        menuEdit->setTitle(QCoreApplication::translate("MainWindow", "Edit", nullptr));
        menuAbout->setTitle(QCoreApplication::translate("MainWindow", "About", nullptr));
        toolBar->setWindowTitle(QCoreApplication::translate("MainWindow", "toolBar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
