using Cytel.Common.Json;
// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model_HZ
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="ParkingInfo.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>ParkingInfo<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

/// <summary>
/// The Model_HZ namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.Model_HZ
{
    /// <summary>
    /// Class ParkingInfo.
    /// </summary>
    public class ParkingInfo
    {
        /// <summary>
        /// 到达时间格式yyyymmddhhmmss.
        /// </summary>
        /// <value>The arrive time.</value>
        [JsonProperty("arrive_time")]
        public string ArriveTime { get; set; }

        /// <summary>
        /// 离开时间格式yyyymmddhhmmss.
        /// </summary>
        /// <value>The departure time.</value>
        [JsonProperty("departure_time")]
        public string DepartureTime { get; set; }

        /// <summary>
        /// 车牌号.
        /// </summary>
        /// <value>The plat number.</value>
        [JsonProperty("plate_number")]
        public string PlatNumber { get; set; }

        /// <summary>
        /// 车类型 小型车1，大型车2，其他3.
        /// 如系统中无此项内容可不传输
        /// </summary>
        /// <value>The type of the car.</value>
        [JsonProperty("car_type")]
        public string CarType { get; set; }

        /// <summary>
        /// 卡号或条码号流水号.
        /// </summary>
        /// <value>The card unique identifier.</value>
        /// 

        [JsonProperty("card_id")]
        public string CardId { get; set; }

        /// <summary>
        /// 停车类型
        /// 计时停车1，全天包月2，白天包月3，晚上包月4，其他5.
        /// </summary>
        /// <value>The type of the card.</value>
        /// 
        [JsonProperty("card_type")]
        public string CardType { get; set; }

        /// <summary>
        /// 剩余泊位数.
        /// </summary>
        /// <value>The spare berth.</value>
        /// 
        [JsonProperty("spare_berth")]
        public string SpareBerth { get; set; }

        /// <summary>
        /// 场内停车数.
        /// </summary>
        /// <value>The parking number.</value>
        /// 
        [JsonProperty("parking_num")]
        public string ParkingNum { get; set; }

        /// <summary>
        /// 停车位编号.
        /// 如系统中无此项内容可不传输
        /// </summary>
        /// <value>The berth code.</value>
        /// 
        [JsonProperty("berth_code")]
        public string BerthCode { get; set; }

        /// <summary>
        /// 状态变更原因.
        /// 车辆到达：1
        /// 车辆离开：2
        /// 车辆逃逸：3
        /// 车辆超时：4
        /// 未刷卡离开：9
        /// 如系统中无此项内容可不传输
        /// </summary>
        /// <value>The change.</value>
        /// 
        [JsonProperty("change")]
        public string Change { get; set; }

        /// <summary>
        /// 泊位状态.
        /// 空闲 0
        /// 车辆预缴费 1
        /// 车辆未缴费 2
        /// 预缴费超时 3
        /// 临时停车 4
        /// 特殊停车 5
        /// 包月车 6
        /// 如系统中无此项内容可不传输
        /// </summary>
        /// <value>The berth status.</value>
        /// 
        [JsonProperty("berth_status")]
        public string BerthStatus { get; set; }
    }
}
