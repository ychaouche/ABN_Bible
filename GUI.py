import wx
import wx.richtext
from Translate import Translate
from Database import find


class abn_bible(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"Angel Broadcasting Network Bible 0.2.3rc1",
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

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        cb_BiblesChoices = ['OLD King James Version (English)',
                            'Bible Society of India (Tamil)',
                            'American King James Version (English)',
                            'Updated King James Version (English)',
                            'American Standard Version (English)',
                            'Darby Version (English)',
                            'Amplified Version (English)',
                            'English Standard Version',
                            'New American Standard Version (English)',
                            'New International Version (English)',
                            'New King James Version (English)',
                            'The Message Version (English)',
                            'New Living Translation (English)',
                            'New Revised Standard Version (English)',
                            'Chinese New Version (Simplified)',
                            'Chinese New Version (Traditional)',
                            'Arabic',
                            'Persian',
                            'Dari (Persian)',
                            'Russian',
                            'Russian Synodal Version',
                            'Portuguese',
                            'La Biblia de las Americas (Spanish)',
                            'Reina Valera (Spanish)',
                            'Reina Valera 1909 (Spanish)',
                            'Amharic (African)',
                            'Sohana (African)',
                            'Ndebele (African)',
                            'Louis Segond (French)']
        self.cb_Bibles = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition,
                                   wx.DefaultSize, cb_BiblesChoices, 0)
        self.cb_Bibles.SetSelection(0)
        bSizer2.Add(self.cb_Bibles, 1, wx.ALL, 5)

        self.btn_Translate = wx.Button(self, wx.ID_ANY,
                                       u"Translate into Indica",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_Translate.Enable(False)

        bSizer2.Add(self.btn_Translate, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        self.FontPicker_src = wx.FontPickerCtrl(self, wx.ID_ANY,
                                                wx.Font(14, 70, 90, 90, False,
                                                        "Arial"),
                                                wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.FNTP_USE_TEXTCTRL)
        self.FontPicker_src.SetMaxPointSize(100)
        bSizer31.Add(self.FontPicker_src, 1, wx.ALL | wx.EXPAND, 5)

        self.btn_Copy_src = wx.Button(self, wx.ID_ANY, u"Copy To Clipboard",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.btn_Copy_src, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer31, 1, wx.EXPAND, 5)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.rtc_Box1 = wx.richtext.RichTextCtrl(self, wx.ID_ANY,
                                                 wx.EmptyString,
                                                 wx.DefaultPosition,
                                                 wx.Size(500, 250),
                                                 0 | wx.VSCROLL | wx.HSCROLL
                                                 | wx.NO_BORDER | wx
                                                 .WANTS_CHARS)
        bSizer1.Add(self.rtc_Box1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.FontPicker_dest = wx.FontPickerCtrl(self, wx.ID_ANY,
                                                 wx.Font(14, 70, 90, 90, False,
                                                         "Arial"),
                                                 wx.DefaultPosition,
                                                 wx.DefaultSize,
                                                 wx.FNTP_USE_TEXTCTRL)
        self.FontPicker_dest.SetMaxPointSize(100)
        self.FontPicker_dest.Enable(False)
        self.FontPicker_dest.Hide()

        bSizer3.Add(self.FontPicker_dest, 1, wx.ALL | wx.EXPAND, 5)

        self.btn_Copy_dest = wx.Button(self, wx.ID_ANY,
                                       u"Copy Translated To Clipboard",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_Copy_dest.Enable(False)
        self.btn_Copy_dest.Hide()

        bSizer3.Add(self.btn_Copy_dest, 0, wx.ALL, 5)

        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)

        self.rtc_Box2 = wx.richtext.RichTextCtrl(self, wx.ID_ANY,
                                                 wx.EmptyString,
                                                 wx.DefaultPosition,
                                                 wx.Size(500, 250),
                                                 0 | wx.VSCROLL | wx.HSCROLL | \
                                                 wx.NO_BORDER | wx.WANTS_CHARS)
        self.rtc_Box2.Enable(False)
        self.rtc_Box2.Hide()

        bSizer1.Add(self.rtc_Box2, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add(bSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.sc.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.Search)
        self.cb_Bibles.Bind(wx.EVT_CHOICE, self.BibleSelected)
        self.btn_Translate.Bind(wx.EVT_BUTTON, self.Translate)
        self.FontPicker_src.Bind(wx.EVT_FONTPICKER_CHANGED,
                                 self.FontChanged_src)
        self.btn_Copy_src.Bind(wx.EVT_BUTTON, self.Copy_src)
        self.FontPicker_dest.Bind(wx.EVT_FONTPICKER_CHANGED, self.FontChanged)
        self.btn_Copy_dest.Bind(wx.EVT_BUTTON, self.Copy)

        #Variables
        self.results = None
        self.multi = True

    def __del__(self):
        pass

    def Clear(self):
        self.multi = False
        self.results = None
        self.rtc_Box1.Clear()
        self.rtc_Box2.Clear()

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
            self.results = find(search_term, 'esv')
        elif choice == 8:
            self.results = find(search_term, 'nasb')
        elif choice == 9:
            self.results = find(search_term, 'niv')
        elif choice == 10:
            self.results = find(search_term, 'nkjv')
        elif choice == 11:
            self.results = find(search_term, 'msg')
        elif choice == 12:
            self.results = find(search_term, 'nlt')
        elif choice == 13:
            self.results = find(search_term, 'nrsv')
        elif choice == 14:
            self.results = find(search_term, 'ch_ncvs')
        elif choice == 15:
            self.results = find(search_term, 'ch_ncvt')
        elif choice == 16:
            self.results = find(search_term, 'arabic')
        elif choice == 17:
            self.results = find(search_term, 'persian')
        elif choice == 18:
            self.results = find(search_term, 'dari')
        elif choice == 19:
            self.results = find(search_term, 'russian')
        elif choice == 20:
            self.results = find(search_term, 'rus_synodal')
        elif choice == 21:
            self.results = find(search_term, 'portuguese')
        elif choice == 22:
            self.results = find(search_term, 'spanish_lbla')
        elif choice == 23:
            self.results = find(search_term, 'spanish_reina')
        elif choice == 24:
            self.results = find(search_term, 'spanish_1909')
        elif choice == 25:
            self.results = find(search_term, 'african_amharic')
        elif choice == 26:
            self.results = find(search_term, 'african_sohana')
        elif choice == 27:
            self.results = find(search_term, 'african_ndebele')
        elif choice == 28:
            self.results = find(search_term, 'french_lsg')
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

    def BibleSelected(self, event):
        if self.sc.GetValue(): self.Search(event)
        if self.cb_Bibles.GetCurrentSelection() == 1:
            self.rtc_Box2.Enable(True)
            self.rtc_Box2.Show()
            self.btn_Copy_dest.Enable(True)
            self.btn_Copy_dest.Show()
            self.FontPicker_dest.Enable(True)
            self.FontPicker_dest.Show()
            self.btn_Translate.Enable()
        else:
            self.rtc_Box2.Enable(False)
            self.rtc_Box2.Hide()
            self.btn_Copy_dest.Enable(False)
            self.btn_Copy_dest.Hide()
            self.FontPicker_dest.Enable(False)
            self.FontPicker_dest.Hide()
            self.btn_Translate.Disable()
        self.Layout()
        event.Skip()

    def Translate(self, event):
        for i in Translate(self.results, self.multi):
            self.rtc_Box2.AppendText(i+'\n')
        self.rtc_Box2.Copy()
        event.Skip()

    def FontChanged_src(self, event):
        selectedFont = self.FontPicker_src.GetSelectedFont()
        self.rtc_Box1.SetFont(selectedFont)
        event.Skip()

    def Copy_src(self, event):
        if self.rtc_Box1.GetSelection() == (-2, -2):
            self.rtc_Box1.SelectAll()
            self.rtc_Box1.Copy()
        else: self.rtc_Box1.Copy()
        event.Skip()

    def FontChanged(self, event):
        selectedFont = self.FontPicker_dest.GetSelectedFont()
        self.rtc_Box2.SetFont(selectedFont)
        event.Skip()

    def Copy(self, event):
        if self.rtc_Box2.GetSelection() == (-2, -2):
            self.rtc_Box2.SelectAll()
            self.rtc_Box2.Copy()
        else: self.rtc_Box2.Copy()
        event.Skip()

def Main():
    app = wx.App(False)
    appFrm = abn_bible(None)
    appFrm.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    Main()