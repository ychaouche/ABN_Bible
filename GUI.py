import wx
import wx.richtext
from Translate import Translate
from Database import find


class abn_bible(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"Angel Broadcasting Network Bible",
                          pos=wx.DefaultPosition, size=wx.Size(600, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer1.AddGrowableCol(0)
        fgSizer1.AddGrowableRow(3)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.sc = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString,
                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.sc.ShowSearchButton(True)
        self.sc.ShowCancelButton(False)
        fgSizer1.Add(self.sc, 1, wx.ALL | wx.EXPAND, 5)

        self.FontPicker = wx.FontPickerCtrl(self, wx.ID_ANY,
                                            wx.Font(14, 70, 90, 90, False,
                                                    "Arial"),
                                            wx.DefaultPosition, wx.DefaultSize,
                                            wx.FNTP_USE_TEXTCTRL)
        self.FontPicker.SetMaxPointSize(100)
        fgSizer1.Add(self.FontPicker, 0, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        cb_BiblesChoices = ['OLD King James Version (English)',
                            'Bible Society of India (Tamil)',
                            'American King James Version (English)',
                            'Updated King James Version (English)',
                            'American Standard Version (English)',
                            'Darby Version (English)',
                            'Amplified Version (English)',
                            'Contemporary English Version',
                            'English Standard Version',
                            'New American Standard Version (English)',
                            'New International Version (English)',
                            'New King James Version (English)',
                            'The Message Version (English)',
                            'New Living Translation (English)',
                            'New Revised Standard Version (English)']
        self.cb_Bibles = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition,
                                   wx.DefaultSize, cb_BiblesChoices, 0)
        self.cb_Bibles.SetSelection(0)
        bSizer2.Add(self.cb_Bibles, 1, wx.ALL, 5)

        self.btn_Translate = wx.Button(self, wx.ID_ANY,
                                       u"Translate into Indica",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_Translate, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.rtc_Box1 = wx.richtext.RichTextCtrl(self, wx.ID_ANY,
                                                 wx.EmptyString,
                                                 wx.DefaultPosition,
                                                 wx.Size(500, 250),
                                                 wx.TE_READONLY | wx.VSCROLL
                                                 | wx.HSCROLL | wx.NO_BORDER
                                                 | wx.WANTS_CHARS)
        bSizer1.Add(self.rtc_Box1, 1, wx.ALL | wx.EXPAND, 5)

        self.btn_Copy = wx.Button(self, wx.ID_ANY, u"Copy To Clipboard",
                                  wx.DefaultPosition, wx.DefaultSize, 0)

        bSizer1.Add(self.btn_Copy, 0, wx.ALL, 5)

        self.rtc_Box2 = wx.richtext.RichTextCtrl(self, wx.ID_ANY,
                                                 wx.EmptyString,
                                                 wx.DefaultPosition,
                                                 wx.Size(500, 250),
                                                 wx.TE_READONLY | \
                                                 wx.VSCROLL | \
                                                 wx.HSCROLL | \
                                                 wx.NO_BORDER | \
                                                 wx.WANTS_CHARS)
        bSizer1.Add(self.rtc_Box2, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add(bSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.sc.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.Search)
        self.FontPicker.Bind(wx.EVT_FONTPICKER_CHANGED, self.FontChanged)
        self.btn_Translate.Bind(wx.EVT_BUTTON, self.Translate)
        self.btn_Copy.Bind(wx.EVT_BUTTON, self.Copy)
        self.results = None
        self.multi = True

    def __del__(self):
        pass

    def Clear(self):
        self.multi = False
        self.results = None
        self.rtc_Box1.Clear()
        self.rtc_Box2.Clear()

    def Copy(self, event):
        self.rtc_Box2.Copy()
        event.Skip()

    # Virtual event handlers, overide them in your derived class
    def Search(self, event):
        self.Clear()
        search_term = str(self.sc.GetValue())
        choice = self.cb_Bibles.GetCurrentSelection()
        if choice == 0:
            self.results = find(search_term, 'kjv')
        elif choice == 1:
            self.results = find(search_term, 'tamil')
        elif choice == 2:
            self.results = find(search_term, 'akjv')
        elif choice == 3:
            self.results = find(search_term, 'ukjv')
        elif choice == 4:
            self.results = find(search_term, 'asv')
        elif choice == 5:
            self.results = find(search_term, 'darby')
        elif choice == 6:
            self.results = find(search_term, 'amp')
        elif choice == 7:
            self.results = find(search_term, 'cev')
        elif choice == 8:
            self.results = find(search_term, 'esv')
        elif choice == 9:
            self.results = find(search_term, 'nasb')
        elif choice == 10:
            self.results = find(search_term, 'niv')
        elif choice == 11:
            self.results = find(search_term, 'nkjv')
        elif choice == 12:
            self.results = find(search_term, 'msg')
        elif choice == 13:
            self.results = find(search_term, 'nlt')
        elif choice == 14:
            self.results = find(search_term, 'nrsv')
        if '-' in search_term:
            self.multi = True
            if self.results:
                for i in self.results:
                    self.rtc_Box1.AppendText(str(i[0])+': '+i[1]+'\n')
        else:
            self.multi = False
            try:
                self.rtc_Box1.AppendText(
                    str(self.results[0])+': '+self.results[1]+'\n')
            except TypeError:
                pass
        event.Skip()

    def FontChanged(self, event):
        selectedFont = self.FontPicker.GetSelectedFont()
        self.rtc_Box2.SetFont(selectedFont)
        event.Skip()

    def Translate(self, event):
        for i in Translate(self.results, self.multi):
            self.rtc_Box2.AppendText(i+'\n')
        self.rtc_Box2.Copy()
        event.Skip()


def Main():
    app = wx.App(False)
    appFrm = abn_bible(None)
    appFrm.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    Main()