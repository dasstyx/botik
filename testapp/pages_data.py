from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage
from testapp.native_args_page import NativeArgsPage
from testapp.phone_page import PhonePage
from testapp.stub_page import StubPage

main_data = PageData(MainPage, '/', '', inline=True, one_time=True)
info_data = PageData(InfoPage, '/info', main_data, inline=False, one_time=False)
phone_data = PageData(PhonePage, '/phone', main_data, inline=False, one_time=False)

nargs_data = PageData(NativeArgsPage, '/nargs', main_data, inline=False, one_time=False)
stub1_data = PageData(StubPage, '/stub1', nargs_data, num=1, inline=False, one_time=False)
stub2_data = PageData(StubPage, '/stub2', stub1_data, num=2, inline=False, one_time=False)