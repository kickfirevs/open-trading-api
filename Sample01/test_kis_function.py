import os
import unittest
import kis_auth as ka
import kis_domstk as kb

class TestAdd(unittest.TestCase):

  def test_get_onedirvepath(self) :
    # 개인용 OneDrive 경로 (기본적으로 사용)
    onedrive_path = os.environ.get("OneDrive")

    # 조직용/업무용 OneDrive 경로 (필요한 경우)
    onedrive_commercial_path = os.environ.get("OneDriveCommercial")

    print("개인 OneDrive 경로:", onedrive_path)
    print("기업용 OneDrive 경로:", onedrive_commercial_path)

    onedrive_private_path  = os.environ.get("OneDrivePrivate")
    print("private", onedrive_private_path)

  def test_Auth(self) :
    ka.auth()
    # [국내주식] 주문/계좌 > 주식잔고조회 (잔고현황)
    rt_data = kb.get_inquire_balance_obj()
    print(rt_data)

    # [국내주식] 주문/계좌 > 매수가능조회 (종목번호 5자리 + 종목단가)
    rt_data = kb.get_inquire_psbl_order(pdno="", ord_unpr=0)
    ord_psbl_cash_value = rt_data.loc[0, 'ord_psbl_cash']  # ord_psbl_cash	주문가능현금
    ord_psbl_cash_value = rt_data.loc[0, 'nrcvb_buy_amt']  # nrcvb_buy_amt	미수없는매수가능금액
    print(rt_data)

    # [국내주식] 기본시세 > 주식현재가 시세 (종목번호 6자리)
    rt_data = kb.get_inquire_price(itm_no="071050")
    print(rt_data.stck_prpr + " " + rt_data.prdy_vrss)  # 현재가, 전일대비


if __name__ == '__main__':
  unittest.main()