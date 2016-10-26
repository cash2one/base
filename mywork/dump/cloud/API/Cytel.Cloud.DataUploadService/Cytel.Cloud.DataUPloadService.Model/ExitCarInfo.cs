using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cytel.Cloud.DataUPloadService.Model
{
   public class ExitCarInfo
    {
        /// <summary>
        /// 车场id.
        /// </summary>
        /// <value>The park unique identifier.</value>
        public string ParkId { get; set; }

        /// <summary>
        /// 出口名称.
        /// </summary>
        /// <value>The name of Exit.</value>
        public string GateName { get; set; }

        /// <summary>
        /// 出场时间.
        /// </summary>
        /// <value>The exittime.</value>
        public DateTime KTime { get; set; }

        /// <summary>
        /// 车辆类型.
        /// </summary>
        /// <value>The car type.</value>
        public int KType { get; set; }

        /// <summary>
        /// 车位数据
        /// </summary>
        /// <value>The entry time.</value>
        public SpaceInfo SpaceInfo { get; set; }

        /// <summary>
        /// 卡号
        /// </summary>
        /// <value>The card number.</value>
        public string CardNo { get; set; }
        /// <summary>
        /// 车牌号码
        /// </summary>
        /// <value>The car number.</value>
        public string PlateNo { get; set; }
        /// <summary>
        ///停车时长
        /// </summary>
        /// <value>The ParkLength.</value>
        public string ParkLength { get; set; }
        /// <summary>
        /// 收费金额
        /// </summary>
        /// <value>The payment.</value>
        public string Charge { get; set; }
        /// <summary>
        /// 支付类型
        /// </summary>
        /// <value>The pay type.</value>
        public int PayType { get; set; }
    }
}
