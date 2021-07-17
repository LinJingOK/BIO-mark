# -*- coding: utf-8 -*-


#将未标注的test文本 以空格划分一次。取后面一部分作为BIO待标注语料

infile = open("../divide/divide_data/dev.txt", "r", encoding="utf-8")
outfile = open("../divide/remove_blank/dev.txt", "w", encoding="utf-8")

lines = infile.readlines()
for line in lines:
    # line = "2014年01月08日16:00 据山东省地震台网测定，1月7日22时24分，我省乳山市发生4.3级地震，烟台市牟平区、栖霞市震感强烈。截止23时30分，没有接到人员伤亡和房屋倒塌的报告。地震专家会商认为，本次地震为正常地震活动事件。  1月7日22时24分，乳山市(东经121.7度，北纬36.8度)发生4.3级地震，威海乳山市、烟台市牟平区、栖霞市震感强烈，荣成等有震感。  大众网记者从山东省地震局了解到，震后，山东省地震局立即启动地震应急预案，召开紧急地震会商会，分析研判震情趋势。同时派出了副局长林金狮带领的9人现场工作队第一时间赶赴震区开展灾害调查、流动地震监测、应急宣传等工作。威海、烟台、青岛市也派出现场工作队赶赴震区开展流动地震监测工作。"

    line = line.split(' ', 1)[1].replace(' ', '')
    print(line)
    outfile.write(line)