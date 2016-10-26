using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Cytel.Cloud.DataInteractiveService.Model;
using Cytel.Cloud.DataInteractiveService.Model_HZ;
using Cytel.Common.Json;
using Cytel.Common.Http;
using System.Configuration;
using Cytel.Common.Log;

namespace Cytel.Cloud.DataInteractiveService.HZ
{
    public class BExit
    {
        public MResponseBase Execute(MRequestBase req)
        {
            MResponseBase resp = new MResponseBase();
            ParkingInfo parkinfo = new ParkingInfo();
            List<ParkingInfo> parklist = new List<ParkingInfo>();

            MExitRequest Mexit = JsonConvert.DeserializeObject<MExitRequest>(req.Data);
            parkinfo.DepartureTime = Mexit.KTime.ToString("yyyyMMddHHmmss");
            parkinfo.CardId = Mexit.CardNo;
            if (Mexit.KType == MCarType.Temp)
                parkinfo.CardType = "1"; 
            else if (Mexit.KType == MCarType.FullDayMonthly)
                parkinfo.CardType = "2";
            else
                parkinfo.CardType = "5";
            parkinfo.SpareBerth = Mexit.SpaceInfo.FSpace.ToString();
            parkinfo.ParkingNum = (Mexit.SpaceInfo.TSpace - Mexit.SpaceInfo.FSpace).ToString();

            Parking parking = new Parking();
            parking.ParkCode = Mexit.ParkId;
            parking.GateName = Mexit.GateName;
            parklist.Add(parkinfo);
            parking.ParkingInfo=parklist;
            //提交
            string postdata = JsonConvert.SerializeObject(parking);
            HttpRequestParam HttpReq = new HttpRequestParam();
            HttpReq.URL = ConfigurationSettings.AppSettings["PostURL"]; ;
            HttpReq.Method = "POST";
            HttpReq.ContentType = "application/json;charset=utf-8";
            HttpReq.Postdata = postdata;
            try
            {
                HttpResult Hresult = HttpHelper.GetHttpRequestData(HttpReq);
                string Mrespone = string.Empty;
                Mrespone = Hresult.Html;
                if (!string.IsNullOrEmpty(Mrespone))
                {

                    ResultInfo resultinfo = new ResultInfo();
                    resultinfo = JsonConvert.DeserializeObject<ResultInfo>(Mrespone);
                    if (resultinfo.status == 201)
                    {
                        resp.Success = true;
                        resp.Code = MResponseCode.Success;
                        resp.Message = "提交成功";
                    }
                    else
                    {
                        resp.Success = false;
                        resp.Code = MResponseCode.SysError;
                        resp.Message = resultinfo.message;
                    }
                    //resp.Data = req.Data;
                    //resp.RequestToken = req.RequestToken;
                    //resp.Sign = req.Sign;
                }
            }
            catch(Exception ex)
            {
                LogWrapper.WriteError(ex.ToString());
                resp.Success = false;
                resp.Code = MResponseCode.SysError;
                resp.Message = "网络问题/数据接收超时"; 
                //resp.Data = req.Data;
                //resp.RequestToken = req.RequestToken;
                //resp.Sign = req.Sign;
            }


            return resp;
        }
    }
}
