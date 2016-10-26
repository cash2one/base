using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Cytel.Cloud.DataUPloadService.Model;
using Cytel.Common.Http;
using Cytel.Common.Json;
using Cytel.Cloud.DataInteractiveService.Model;
using Cytel.Common.Log;

namespace Cytel.Cloud.DataUPloadService.Interactive
{
    public class MessageUploader
    {
        public static string PostJson(string MRequest,string URL)
        {
            string Mrespone="";
            try
            {               
                HttpRequestParam HttpReq = new HttpRequestParam();
                HttpReq.URL = URL;
                HttpReq.Method = "POST";
                HttpReq.ContentType = "application/json;charset=utf-8";
                HttpReq.Postdata = MRequest;
                HttpResult Hresult= HttpHelper.GetHttpRequestData(HttpReq);
                Mrespone=Hresult.Html;
            }
            catch(Exception ex)
            {
                LogWrapper.WriteError(ex.ToString());
            }
            return Mrespone;
        }  
    }
}
