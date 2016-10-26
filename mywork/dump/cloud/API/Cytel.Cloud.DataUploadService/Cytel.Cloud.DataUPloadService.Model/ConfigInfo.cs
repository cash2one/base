using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cytel.Cloud.DataUPloadService.Model
{
   public class ConfigInfo
    {
        /// <summary>
        /// 监听端口
        /// </summary>
        /// <value>The Listen Port.</value>
       public int ListenPort { get; set; }

        /// <summary>
        /// 服务器ip.
        /// </summary>
        /// <value>The ip of vbmserver.</value>
        public string VBMServer { get; set; }

        /// <summary>
        /// 停车场id.
        /// </summary>
        /// <value>The id of parking.</value>
        public string ParkID { get; set; }
       /// <summary>
       /// 业务请求
       /// </summary>
        public string POSTURL { get; set; }
        public string Serect { get; set; }

    }
}
