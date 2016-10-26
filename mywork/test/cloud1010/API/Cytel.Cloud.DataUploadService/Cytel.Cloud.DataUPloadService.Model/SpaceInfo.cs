using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cytel.Cloud.DataUPloadService.Model
{
   public class SpaceInfo
    {
        /// <summary>
        /// 总车位.
        /// </summary>
        /// <value>The Total space.</value>
        public int TSpace { get; set; }

        /// <summary>
        /// 剩余总车位.
        /// </summary>
        /// <value>The left Total space.</value>
        public int FSpace { get; set; }

        /// <summary>
        /// 总月租车位.
        /// </summary>
        /// <value>The total monthly space.</value>
        public int TMonthly { get; set; }

        /// <summary>
        /// 剩余月租总车位.
        /// </summary>
        /// <value>The left total monthly space.</value>
        public int FMonthly { get; set; }

        /// <summary>
        /// 时租总车位
        /// </summary>
        /// <value>The total hourly space.</value>
        public int TTemp { get; set; }

        /// <summary>
        /// 剩余时租总车位
        /// </summary>
        /// <value>The left total hourly space.</value>
        public int FTemp { get; set; }

    }
}
