import logging
from fyers_api import fyersModel, accessToken

from config.Config import getSystemConfig
from loginmgmt.BaseLogin import BaseLogin

class FyersLogin(BaseLogin):
  def __init__(self, brokerAppDetails):
    BaseLogin.__init__(self, brokerAppDetails)

  def login(self, args):
    logging.info('==> FyersLogin .args => %s', args)
    systemConfig = getSystemConfig()
    # accessToken = accessToken()
    session=accessToken.SessionModel(client_id=self.brokerAppDetails.clientID, secret_key=self.brokerAppDetails.appKey, redirect_uri=self.brokerAppDetails.redirectURL, response_type="code", grant_type="authorization_code")
    response = session.generate_authcode()
    # brokerHandle = KiteConnect(api_key=)
    redirectUrl = None
    if 'request_token' in args:
      requestToken = args['request_token']
      logging.info('Fyers requestToken = %s', requestToken)
      session = brokerHandle.generate_session(requestToken, api_secret=self.brokerAppDetails.appSecret)
      
      accessToken = session['access_token']
      accessToken = accessToken
      logging.info('Fyers accessToken = %s', accessToken)
      brokerHandle.set_access_token(accessToken)
      
      logging.info('Fyers Login successful. accessToken = %s', accessToken)

      # set broker handle and access token to the instance
      self.setBrokerHandle(brokerHandle)
      self.setAccessToken(accessToken)

      # redirect to home page with query param loggedIn=true
      homeUrl = systemConfig['homeUrl'] + '?loggedIn=true'
      logging.info('Fyers Redirecting to home page %s', homeUrl)
      redirectUrl = homeUrl
    else:
      loginUrl = brokerHandle.login_url()
      logging.info('Redirecting to Fyers login url = %s', loginUrl)
      redirectUrl = loginUrl

    return redirectUrl

