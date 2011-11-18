#!/usr/bin/python 
from Baseclass import *
from mov import *
from arithmetics import *
from jmp import *
from decode_logical import *


def runner():
	pcntr_run = 0
	while pcntr_run < UC.PC:
			
		if UC.ROM[pcntr_run] == '00':
			pcntr_run=OP_00(pcntr_run)
		elif UC.ROM[pcntr_run] == '01':
			pcntr_run=OP_01(pcntr_run)
		elif UC.ROM[pcntr_run] == '02':
			pcntr_run=OP_02(pcntr_run)
		elif UC.ROM[pcntr_run] == '03':
			pcntr_run=OP_03(pcntr_run)
		elif UC.ROM[pcntr_run] == '04':
			pcntr_run=OP_04(pcntr_run)
		elif UC.ROM[pcntr_run] == '05':
			pcntr_run=OP_05(pcntr_run)
		elif UC.ROM[pcntr_run] == '06':
			pcntr_run=OP_06(pcntr_run)
		elif UC.ROM[pcntr_run] == '07':
			pcntr_run=OP_07(pcntr_run)
		elif UC.ROM[pcntr_run] == '08':
			pcntr_run=OP_08(pcntr_run)
		elif UC.ROM[pcntr_run] == '09':
			pcntr_run=OP_09(pcntr_run)
		elif UC.ROM[pcntr_run] == '0A':
			pcntr_run=OP_0A(pcntr_run)
		elif UC.ROM[pcntr_run] == '0B':
			pcntr_run=OP_0B(pcntr_run)
		elif UC.ROM[pcntr_run] == '0C':
			pcntr_run=OP_0C(pcntr_run)
		elif UC.ROM[pcntr_run] == '0D':
			pcntr_run=OP_0D(pcntr_run)
		elif UC.ROM[pcntr_run] == '0E':
			pcntr_run=OP_0E(pcntr_run)
		elif UC.ROM[pcntr_run] == '0F':
			pcntr_run=OP_0F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '10':
			pcntr_run=OP_10(pcntr_run)
		elif UC.ROM[pcntr_run] == '11':
			pcntr_run=OP_11(pcntr_run)
		elif UC.ROM[pcntr_run] == '12':
			pcntr_run=OP_12(pcntr_run)
		elif UC.ROM[pcntr_run] == '13':
			pcntr_run=OP_13(pcntr_run)
		elif UC.ROM[pcntr_run] == '14':
			pcntr_run=OP_14(pcntr_run)
		elif UC.ROM[pcntr_run] == '15':
			pcntr_run=OP_15(pcntr_run)
		elif UC.ROM[pcntr_run] == '16':
			pcntr_run=OP_16(pcntr_run)
		elif UC.ROM[pcntr_run] == '17':
			pcntr_run=OP_17(pcntr_run)
		elif UC.ROM[pcntr_run] == '18':
			pcntr_run=OP_18(pcntr_run)
		elif UC.ROM[pcntr_run] == '19':
			pcntr_run=OP_19(pcntr_run)
		elif UC.ROM[pcntr_run] == '1A':
			pcntr_run=OP_1A(pcntr_run)
		elif UC.ROM[pcntr_run] == '1B':
			pcntr_run=OP_1B(pcntr_run)
		elif UC.ROM[pcntr_run] == '1C':
			pcntr_run=OP_1C(pcntr_run)
		elif UC.ROM[pcntr_run] == '1D':
			pcntr_run=OP_1D(pcntr_run)
		elif UC.ROM[pcntr_run] == '1E':
			pcntr_run=OP_1E(pcntr_run)
		elif UC.ROM[pcntr_run] == '1F':
			pcntr_run=OP_1F(pcntr_run)

		elif UC.ROM[pcntr_run] == '20':
			pcntr_run=OP_20(pcntr_run)
		elif UC.ROM[pcntr_run] == '21':
			pcntr_run=OP_21(pcntr_run)
		elif UC.ROM[pcntr_run] == '22':
			pcntr_run=OP_22(pcntr_run)
		elif UC.ROM[pcntr_run] == '23':
			pcntr_run=OP_23(pcntr_run)
		elif UC.ROM[pcntr_run] == '24':
			pcntr_run=OP_24(pcntr_run)
		elif UC.ROM[pcntr_run] == '25':
			pcntr_run=OP_25(pcntr_run)
		elif UC.ROM[pcntr_run] == '26':
			pcntr_run=OP_26(pcntr_run)
		elif UC.ROM[pcntr_run] == '27':
			pcntr_run=OP_27(pcntr_run)
		elif UC.ROM[pcntr_run] == '28':
			pcntr_run=OP_28(pcntr_run)
		elif UC.ROM[pcntr_run] == '29':
			pcntr_run=OP_29(pcntr_run)
		elif UC.ROM[pcntr_run] == '2A':
			pcntr_run=OP_2A(pcntr_run)
		elif UC.ROM[pcntr_run] == '2B':
			pcntr_run=OP_2B(pcntr_run)
		elif UC.ROM[pcntr_run] == '2C':
			pcntr_run=OP_2C(pcntr_run)
		elif UC.ROM[pcntr_run] == '2D':
			pcntr_run=OP_2D(pcntr_run)
		elif UC.ROM[pcntr_run] == '2E':
			pcntr_run=OP_2E(pcntr_run)
		elif UC.ROM[pcntr_run] == '2F':
			pcntr_run=OP_2F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '30':
			pcntr_run=OP_30(pcntr_run)
		elif UC.ROM[pcntr_run] == '31':
			pcntr_run=OP_31(pcntr_run)
		elif UC.ROM[pcntr_run] == '32':
			pcntr_run=OP_32(pcntr_run)
		elif UC.ROM[pcntr_run] == '33':
			pcntr_run=OP_33(pcntr_run)
		elif UC.ROM[pcntr_run] == '34':
			pcntr_run=OP_34(pcntr_run)
		elif UC.ROM[pcntr_run] == '35':
			pcntr_run=OP_35(pcntr_run)
		elif UC.ROM[pcntr_run] == '36':
			pcntr_run=OP_36(pcntr_run)
		elif UC.ROM[pcntr_run] == '37':
			pcntr_run=OP_37(pcntr_run)
		elif UC.ROM[pcntr_run] == '38':
			pcntr_run=OP_38(pcntr_run)
		elif UC.ROM[pcntr_run] == '39':
			pcntr_run=OP_39(pcntr_run)
		elif UC.ROM[pcntr_run] == '3A':
			pcntr_run=OP_3A(pcntr_run)
		elif UC.ROM[pcntr_run] == '3B':
			pcntr_run=OP_3B(pcntr_run)
		elif UC.ROM[pcntr_run] == '3C':
			pcntr_run=OP_3C(pcntr_run)
		elif UC.ROM[pcntr_run] == '3D':
			pcntr_run=OP_3D(pcntr_run)
		elif UC.ROM[pcntr_run] == '3E':
			pcntr_run=OP_3E(pcntr_run)
		elif UC.ROM[pcntr_run] == '3F':
			pcntr_run=OP_3F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '40':
			pcntr_run=OP_40(pcntr_run)
		elif UC.ROM[pcntr_run] == '41':
			pcntr_run=OP_41(pcntr_run)
		elif UC.ROM[pcntr_run] == '42':
			pcntr_run=OP_42(pcntr_run)
		elif UC.ROM[pcntr_run] == '43':
			pcntr_run=OP_43(pcntr_run)
		elif UC.ROM[pcntr_run] == '44':
			pcntr_run=OP_44(pcntr_run)
		elif UC.ROM[pcntr_run] == '45':
			pcntr_run=OP_45(pcntr_run)
		elif UC.ROM[pcntr_run] == '46':
			pcntr_run=OP_46(pcntr_run)
		elif UC.ROM[pcntr_run] == '47':
			pcntr_run=OP_47(pcntr_run)
		elif UC.ROM[pcntr_run] == '48':
			pcntr_run=OP_48(pcntr_run)
		elif UC.ROM[pcntr_run] == '49':
			pcntr_run=OP_49(pcntr_run)
		elif UC.ROM[pcntr_run] == '4A':
			pcntr_run=OP_4A(pcntr_run)
		elif UC.ROM[pcntr_run] == '4B':
			pcntr_run=OP_4B(pcntr_run)
		elif UC.ROM[pcntr_run] == '4C':
			pcntr_run=OP_4C(pcntr_run)
		elif UC.ROM[pcntr_run] == '4D':
			pcntr_run=OP_4D(pcntr_run)
		elif UC.ROM[pcntr_run] == '4E':
			pcntr_run=OP_4E(pcntr_run)
		elif UC.ROM[pcntr_run] == '4F':
			pcntr_run=OP_4F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '50':
			pcntr_run=OP_50(pcntr_run)
		elif UC.ROM[pcntr_run] == '51':
			pcntr_run=OP_51(pcntr_run)
		elif UC.ROM[pcntr_run] == '52':
			pcntr_run=OP_52(pcntr_run)
		elif UC.ROM[pcntr_run] == '53':
			pcntr_run=OP_53(pcntr_run)
		elif UC.ROM[pcntr_run] == '54':
			pcntr_run=OP_54(pcntr_run)
		elif UC.ROM[pcntr_run] == '55':
			pcntr_run=OP_55(pcntr_run)
		elif UC.ROM[pcntr_run] == '56':
			pcntr_run=OP_56(pcntr_run)
		elif UC.ROM[pcntr_run] == '57':
			pcntr_run=OP_57(pcntr_run)
		elif UC.ROM[pcntr_run] == '58':
			pcntr_run=OP_58(pcntr_run)
		elif UC.ROM[pcntr_run] == '59':
			pcntr_run=OP_59(pcntr_run)
		elif UC.ROM[pcntr_run] == '5A':
			pcntr_run=OP_5A(pcntr_run)
		elif UC.ROM[pcntr_run] == '5B':
			pcntr_run=OP_5B(pcntr_run)
		elif UC.ROM[pcntr_run] == '5C':
			pcntr_run=OP_5C(pcntr_run)
		elif UC.ROM[pcntr_run] == '5D':
			pcntr_run=OP_5D(pcntr_run)
		elif UC.ROM[pcntr_run] == '5E':
			pcntr_run=OP_5E(pcntr_run)
		elif UC.ROM[pcntr_run] == '5F':
			pcntr_run=OP_5F(pcntr_run)

		elif UC.ROM[pcntr_run] == '60':
			pcntr_run=OP_60(pcntr_run)
		elif UC.ROM[pcntr_run] == '61':
			pcntr_run=OP_61(pcntr_run)
		elif UC.ROM[pcntr_run] == '62':
			pcntr_run=OP_62(pcntr_run)
		elif UC.ROM[pcntr_run] == '63':
			pcntr_run=OP_63(pcntr_run)
		elif UC.ROM[pcntr_run] == '64':
			pcntr_run=OP_64(pcntr_run)
		elif UC.ROM[pcntr_run] == '65':
			pcntr_run=OP_65(pcntr_run)
		elif UC.ROM[pcntr_run] == '66':
			pcntr_run=OP_66(pcntr_run)
		elif UC.ROM[pcntr_run] == '67':
			pcntr_run=OP_67(pcntr_run)
		elif UC.ROM[pcntr_run] == '68':
			pcntr_run=OP_68(pcntr_run)
		elif UC.ROM[pcntr_run] == '69':
			pcntr_run=OP_69(pcntr_run)
		elif UC.ROM[pcntr_run] == '6A':
			pcntr_run=OP_6A(pcntr_run)
		elif UC.ROM[pcntr_run] == '6B':
			pcntr_run=OP_6B(pcntr_run)
		elif UC.ROM[pcntr_run] == '6C':
			pcntr_run=OP_6C(pcntr_run)
		elif UC.ROM[pcntr_run] == '6D':
			pcntr_run=OP_6D(pcntr_run)
		elif UC.ROM[pcntr_run] == '6E':
			pcntr_run=OP_6E(pcntr_run)
		elif UC.ROM[pcntr_run] == '6F':
			pcntr_run=OP_6F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '70':
			pcntr_run=OP_70(pcntr_run)
		elif UC.ROM[pcntr_run] == '71':
			pcntr_run=OP_71(pcntr_run)
		elif UC.ROM[pcntr_run] == '72':
			pcntr_run=OP_72(pcntr_run)
		elif UC.ROM[pcntr_run] == '73':
			pcntr_run=OP_73(pcntr_run)
		elif UC.ROM[pcntr_run] == '74':
			pcntr_run=OP_74(pcntr_run)
		elif UC.ROM[pcntr_run] == '75':
			pcntr_run=OP_75(pcntr_run)
		elif UC.ROM[pcntr_run] == '76':
			pcntr_run=OP_76(pcntr_run)
		elif UC.ROM[pcntr_run] == '77':
			pcntr_run=OP_77(pcntr_run)
		elif UC.ROM[pcntr_run] == '78':
			pcntr_run=OP_78(pcntr_run)
		elif UC.ROM[pcntr_run] == '79':
			pcntr_run=OP_79(pcntr_run)
		elif UC.ROM[pcntr_run] == '7A':
			pcntr_run=OP_7A(pcntr_run)
		elif UC.ROM[pcntr_run] == '7B':
			pcntr_run=OP_7B(pcntr_run)
		elif UC.ROM[pcntr_run] == '7C':
			pcntr_run=OP_7C(pcntr_run)
		elif UC.ROM[pcntr_run] == '7D':
			pcntr_run=OP_7D(pcntr_run)
		elif UC.ROM[pcntr_run] == '7E':
			pcntr_run=OP_7E(pcntr_run)
		elif UC.ROM[pcntr_run] == '7F':
			pcntr_run=OP_7F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '80':
			pcntr_run=OP_80(pcntr_run)
		elif UC.ROM[pcntr_run] == '81':
			pcntr_run=OP_81(pcntr_run)
		elif UC.ROM[pcntr_run] == '82':
			pcntr_run=OP_82(pcntr_run)
		elif UC.ROM[pcntr_run] == '83':
			pcntr_run=OP_83(pcntr_run)
		elif UC.ROM[pcntr_run] == '84':
			pcntr_run=OP_84(pcntr_run)
		elif UC.ROM[pcntr_run] == '85':
			pcntr_run=OP_85(pcntr_run)
		elif UC.ROM[pcntr_run] == '86':
			pcntr_run=OP_86(pcntr_run)
		elif UC.ROM[pcntr_run] == '87':
			pcntr_run=OP_87(pcntr_run)
		elif UC.ROM[pcntr_run] == '88':
			pcntr_run=OP_88(pcntr_run)
		elif UC.ROM[pcntr_run] == '89':
			pcntr_run=OP_89(pcntr_run)
		elif UC.ROM[pcntr_run] == '8A':
			pcntr_run=OP_8A(pcntr_run)
		elif UC.ROM[pcntr_run] == '8B':
			pcntr_run=OP_8B(pcntr_run)
		elif UC.ROM[pcntr_run] == '8C':
			pcntr_run=OP_8C(pcntr_run)
		elif UC.ROM[pcntr_run] == '8D':
			pcntr_run=OP_8D(pcntr_run)
		elif UC.ROM[pcntr_run] == '8E':
			pcntr_run=OP_8E(pcntr_run)
		elif UC.ROM[pcntr_run] == '8F':
			pcntr_run=OP_8F(pcntr_run)
	
		elif UC.ROM[pcntr_run] == '90':
			pcntr_run=OP_90(pcntr_run)
		elif UC.ROM[pcntr_run] == '91':
			pcntr_run=OP_91(pcntr_run)
		elif UC.ROM[pcntr_run] == '92':
			pcntr_run=OP_92(pcntr_run)
		elif UC.ROM[pcntr_run] == '93':
			pcntr_run=OP_93(pcntr_run)
		elif UC.ROM[pcntr_run] == '94':
			pcntr_run=OP_94(pcntr_run)
		elif UC.ROM[pcntr_run] == '95':
			pcntr_run=OP_95(pcntr_run)
		elif UC.ROM[pcntr_run] == '96':
			pcntr_run=OP_96(pcntr_run)
		elif UC.ROM[pcntr_run] == '97':
			pcntr_run=OP_97(pcntr_run)
		elif UC.ROM[pcntr_run] == '98':
			pcntr_run=OP_98(pcntr_run)
		elif UC.ROM[pcntr_run] == '99':
			pcntr_run=OP_99(pcntr_run)
		elif UC.ROM[pcntr_run] == '9A':
			pcntr_run=OP_9A(pcntr_run)
		elif UC.ROM[pcntr_run] == '9B':
			pcntr_run=OP_9B(pcntr_run)
		elif UC.ROM[pcntr_run] == '9C':
			pcntr_run=OP_9C(pcntr_run)
		elif UC.ROM[pcntr_run] == '9D':
			pcntr_run=OP_9D(pcntr_run)
		elif UC.ROM[pcntr_run] == '9E':
			pcntr_run=OP_9E(pcntr_run)
		elif UC.ROM[pcntr_run] == '9F':
			pcntr_run=OP_9F(pcntr_run)
		
		elif UC.ROM[pcntr_run] == 'A0':
			pcntr_run=OP_A0(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A1':
			pcntr_run=OP_A1(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A2':
			pcntr_run=OP_A2(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A3':
			pcntr_run=OP_A3(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A4':
			pcntr_run=OP_A4(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A5':
			pcntr_run=OP_A5(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A6':
			pcntr_run=OP_A6(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A7':
			pcntr_run=OP_A7(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A8':
			pcntr_run=OP_A8(pcntr_run)
		elif UC.ROM[pcntr_run] == 'A9':
			pcntr_run=OP_A9(pcntr_run)
		elif UC.ROM[pcntr_run] == 'AA':
			pcntr_run=OP_AA(pcntr_run)
		elif UC.ROM[pcntr_run] == 'AB':
			pcntr_run=OP_AB(pcntr_run)
		elif UC.ROM[pcntr_run] == 'AC':
			pcntr_run=OP_AC(pcntr_run)
		elif UC.ROM[pcntr_run] == 'AD':
			pcntr_run=OP_AD(pcntr_run)
		elif UC.ROM[pcntr_run] == 'AE':
			pcntr_run=OP_AE(pcntr_run)
		elif UC.ROM[pcntr_run] == 'AF':
			pcntr_run=OP_AF(pcntr_run)
	
		elif UC.ROM[pcntr_run] == 'B0':
			pcntr_run=OP_B0(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B1':
			pcntr_run=OP_B1(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B2':
			pcntr_run=OP_B2(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B3':
			pcntr_run=OP_B3(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B4':
			pcntr_run=OP_B4(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B5':
			pcntr_run=OP_B5(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B6':
			pcntr_run=OP_B6(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B7':
			pcntr_run=OP_B7(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B8':
			pcntr_run=OP_B8(pcntr_run)
		elif UC.ROM[pcntr_run] == 'B9':
			pcntr_run=OP_B9(pcntr_run)
		elif UC.ROM[pcntr_run] == 'BA':
			pcntr_run=OP_BA(pcntr_run)
		elif UC.ROM[pcntr_run] == 'BB':
			pcntr_run=OP_BB(pcntr_run)
		elif UC.ROM[pcntr_run] == 'BC':
			pcntr_run=OP_BC(pcntr_run)
		elif UC.ROM[pcntr_run] == 'BD':
			pcntr_run=OP_BD(pcntr_run)
		elif UC.ROM[pcntr_run] == 'BE':
			pcntr_run=OP_BE(pcntr_run)
		elif UC.ROM[pcntr_run] == 'BF':
			pcntr_run=OP_BF(pcntr_run)
	
		elif UC.ROM[pcntr_run] == 'C0':
			pcntr_run=OP_C0(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C1':
			pcntr_run=OP_C1(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C2':
			pcntr_run=OP_C2(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C3':
			pcntr_run=OP_C3(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C4':
			pcntr_run=OP_C4(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C5':
			pcntr_run=OP_C5(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C6':
			pcntr_run=OP_C6(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C7':
			pcntr_run=OP_C7(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C8':
			pcntr_run=OP_C8(pcntr_run)
		elif UC.ROM[pcntr_run] == 'C9':
			pcntr_run=OP_C9(pcntr_run)
		elif UC.ROM[pcntr_run] == 'CA':
			pcntr_run=OP_CA(pcntr_run)
		elif UC.ROM[pcntr_run] == 'CB':
			pcntr_run=OP_CB(pcntr_run)
		elif UC.ROM[pcntr_run] == 'CC':
			pcntr_run=OP_CC(pcntr_run)
		elif UC.ROM[pcntr_run] == 'CD':
			pcntr_run=OP_CD(pcntr_run)
		elif UC.ROM[pcntr_run] == 'CE':
			pcntr_run=OP_CE(pcntr_run)
		elif UC.ROM[pcntr_run] == 'CF':
			pcntr_run=OP_CF(pcntr_run)
	
		elif UC.ROM[pcntr_run] == 'D0':
			pcntr_run=OP_D0(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D1':
			pcntr_run=OP_D1(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D2':
			pcntr_run=OP_D2(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D3':
			pcntr_run=OP_D3(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D4':
			pcntr_run=OP_D4(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D5':
			pcntr_run=OP_D5(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D6':
			pcntr_run=OP_D6(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D7':
			pcntr_run=OP_D7(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D8':
			pcntr_run=OP_D8(pcntr_run)
		elif UC.ROM[pcntr_run] == 'D9':
			pcntr_run=OP_D9(pcntr_run)
		elif UC.ROM[pcntr_run] == 'DA':
			pcntr_run=OP_DA(pcntr_run)
		elif UC.ROM[pcntr_run] == 'DB':
			pcntr_run=OP_DB(pcntr_run)
		elif UC.ROM[pcntr_run] == 'DC':
			pcntr_run=OP_DC(pcntr_run)
		elif UC.ROM[pcntr_run] == 'DD':
			pcntr_run=OP_DD(pcntr_run)
		elif UC.ROM[pcntr_run] == 'DE':
			pcntr_run=OP_DE(pcntr_run)
		elif UC.ROM[pcntr_run] == 'DF':
			pcntr_run=OP_DF(pcntr_run)
	
		elif UC.ROM[pcntr_run] == 'E0':
			pcntr_run=OP_E0(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E1':
			pcntr_run=OP_E1(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E2':
			pcntr_run=OP_E2(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E3':
			pcntr_run=OP_E3(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E4':
			pcntr_run=OP_E4(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E5':
			pcntr_run=OP_E5(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E6':
			pcntr_run=OP_E6(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E7':
			pcntr_run=OP_E7(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E8':
			pcntr_run=OP_E8(pcntr_run)
		elif UC.ROM[pcntr_run] == 'E9':
			pcntr_run=OP_E9(pcntr_run)
		elif UC.ROM[pcntr_run] == 'EA':
			pcntr_run=OP_EA(pcntr_run)
		elif UC.ROM[pcntr_run] == 'EB':
			pcntr_run=OP_EB(pcntr_run)
		elif UC.ROM[pcntr_run] == 'EC':
			pcntr_run=OP_EC(pcntr_run)
		elif UC.ROM[pcntr_run] == 'ED':
			pcntr_run=OP_ED(pcntr_run)
		elif UC.ROM[pcntr_run] == 'EE':
			pcntr_run=OP_EE(pcntr_run)
		elif UC.ROM[pcntr_run] == 'EF':
			pcntr_run=OP_EF(pcntr_run)
	
		elif UC.ROM[pcntr_run] == 'F0':
			pcntr_run=OP_F0(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F1':
			pcntr_run=OP_F1(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F2':
			pcntr_run=OP_F2(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F3':
			pcntr_run=OP_F3(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F4':
			pcntr_run=OP_F4(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F5':
			pcntr_run=OP_F5(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F6':
			pcntr_run=OP_F6(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F7':
			pcntr_run=OP_F7(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F8':
			pcntr_run=OP_F8(pcntr_run)
		elif UC.ROM[pcntr_run] == 'F9':
			pcntr_run=OP_F9(pcntr_run)
		elif UC.ROM[pcntr_run] == 'FA':
			pcntr_run=OP_FA(pcntr_run)
		elif UC.ROM[pcntr_run] == 'FB':
			pcntr_run=OP_FB(pcntr_run)
		elif UC.ROM[pcntr_run] == 'FC':
			pcntr_run=OP_FC(pcntr_run)
		elif UC.ROM[pcntr_run] == 'FD':
			pcntr_run=OP_FD(pcntr_run)
		elif UC.ROM[pcntr_run] == 'FE':
			pcntr_run=OP_FE(pcntr_run)
		elif UC.ROM[pcntr_run] == 'FF':
			pcntr_run=OP_FF(pcntr_run)




		

