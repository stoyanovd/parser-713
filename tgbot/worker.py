from splinter import Browser

from tgbot.chrome import get_chrome

def goes():
    browser = get_chrome()
    with Browser() as browser:
        # Visit URL
        url = "https://bankrot.fedresurs.ru/Messages.aspx"
        browser.visit(url)

        elem = browser.find_by_id('ctl00_cphBody_mdsMessageType_tbSelectedText')
        elem.click()

        # browser.fill('q', 'splinter - python acceptance testing for web applications')

        elem = browser.find_by_text('Сообщение о судебном акте')
        elem.click()

        elem = browser.find_by_id('ctl00_cphBody_ibMessagesSearch')
        elem.click()

        # elem = browser.find_by_id('ctl00_cphBody_lnkbtnExcelExport')
        # elem.click()

        elem = browser.find_by_xpath('// *[ @ id = "ctl00_cphBody_gvMessages"] / tbody / tr[2]')

        t = str(elem.__dict__)

        t = t[:3000]

    return t
