<?php
    $arr = [23,12,45,78,56,9];
    $temp = []; $i = 1;
    foreach($arr as $val){
        if(isset($arr[$i+1]) && $arr[$i] < $val){
            array_push($temp, $val);
        }
        print_r($val);
        $i++;
    }
    print_r($temp);