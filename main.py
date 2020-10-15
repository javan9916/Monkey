import wx

from Window import Window


def main():
    app = wx.App()
    frame = Window(None, "Untitled - Codepad")
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()