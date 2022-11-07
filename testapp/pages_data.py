from src.core.page.page_data import PageData
from testapp.pages.main_page import MainPage
from testapp.pages.native_args_page import NativeArgsPage
from testapp.pages.phone_page import PhonePage
from testapp.pages.stub_page import StubPage

main_data = PageData(MainPage, '/', '', inline=True, one_time=True)
phone_data = PageData(PhonePage, '/phone', main_data, inline=False, one_time=False)

nargs_data = PageData(NativeArgsPage, '/nargs', main_data, inline=False, one_time=False)
stub1_data = PageData(StubPage, '/stub1', main_data, num=1, inline=False, one_time=False)
stub2_data = PageData(StubPage, '/stub2', stub1_data, num=2, inline=False, one_time=False)
