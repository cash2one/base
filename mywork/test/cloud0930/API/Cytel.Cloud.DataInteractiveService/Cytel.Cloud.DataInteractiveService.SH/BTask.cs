using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Cytel.Cloud.DataInteractiveService.BizIF;
using Cytel.Cloud.DataInteractiveService.Model;
using Cytel.Common.Json;

namespace Cytel.Cloud.DataInteractiveService.SH
{
    /// <summary>
    /// Class BTask.
    /// </summary>
    public class BTask : ITask
    {

        #region ITask 成员

        /// <summary>
        /// Executes the specified string req.
        /// </summary>
        /// <param name="strReq">The string req.</param>
        /// <returns>System.String.</returns>
        public string Execute(string strReq)
        {
            string strResp = string.Empty;
            MRequestBase req = JsonConvert.DeserializeObject<MRequestBase>(strReq);
            MResponseBase resp = ExecuteObj(req);
            strResp = JsonConvert.SerializeObject(resp);
            return strResp;
        }

        /// <summary>
        /// Executes the object.
        /// </summary>
        /// <param name="req">The req.</param>
        /// <returns>Cytel.Cloud.DataInteractiveService.Model.MResponseBase.</returns>
        private static MResponseBase ExecuteObj(MRequestBase req)
        {
            MResponseBase resp = new MResponseBase();
            switch (req.Method)
            {
                case "enter":
                    resp = new BEnter().Execute(req);
                    break;
                case "exit":
                    resp = new BExit().Execute(req);
                    break;
                case "spacenum":
                   // resp = new BEnter().Execute(req);
                    break;
                case "sysstatus":
                    //resp = new BEnter().Execute(req);
                    break;
                default:
                    resp.Code = MResponseCode.MethodNotFound;
                    resp.Success = false;
                    break;
            }

            return resp;
        }

        #endregion
    }
}
