// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MCarType.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MCarType<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

/// <summary>
/// The Model namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.Model
{
    /// <summary>
    /// Enum MCarType
    /// </summary>
    public enum MCarType
    {
        /// <summary>
        /// 全天包月车辆
        /// </summary>
        FullDayMonthly = 100,

        /// <summary>
        /// 白天包月车辆
        /// </summary>
        DayMonthly,

        /// <summary>
        /// 晚上包月车辆
        /// </summary>
        NightMonthly,

        /// <summary>
        /// 时租访客车辆
        /// </summary>
        Temp = 200,

        /// <summary>
        /// 免费车辆
        /// </summary>
        Free = 300,

        /// <summary>
        /// 异常未知车辆
        /// </summary>
        Unknown = 400
    }
}
