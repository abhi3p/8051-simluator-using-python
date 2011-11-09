from pylab import *
from Baseclass import *
from mov import *
#from arithmetics import *
from jmp import *
from decode_logical import *

UC.PC = 5
pcntr = 0
while pcntr < UC.PC:
	if UC.ROM[pcntr] == '00':
		OP_00(pcntr)
	elif UC.ROM[pcntr] == '01':
		OP_01(pcntr)
	elif UC.ROM[pcntr] == '02':
		OP_02(pcntr)
	elif UC.ROM[pcntr] == '03':
		OP_03(pcntr)
	elif UC.ROM[pcntr] == '04':
		OP_04(pcntr)
	elif UC.ROM[pcntr] == '05':
		OP_05(pcntr)
	elif UC.ROM[pcntr] == '06':
		OP_06(pcntr)
	elif UC.ROM[pcntr] == '07':
		OP_07(pcntr)
	elif UC.ROM[pcntr] == '08':
		OP_08(pcntr)
	elif UC.ROM[pcntr] == '09':
		OP_09(pcntr)
	elif UC.ROM[pcntr] == '0A':
		OP_0A(pcntr)
	elif UC.ROM[pcntr] == '0B':
		OP_0B(pcntr)
	elif UC.ROM[pcntr] == '0C':
		OP_0C(pcntr)
	elif UC.ROM[pcntr] == '0D':
		OP_0D(pcntr)
	elif UC.ROM[pcntr] == '0E':
		OP_0E(pcntr)
	elif UC.ROM[pcntr] == '0F':
		OP_0F(pcntr)
	
	elif UC.ROM[pcntr] == '10':
		OP_10(pcntr)
	elif UC.ROM[pcntr] == '11':
		OP_11(pcntr)
	elif UC.ROM[pcntr] == '12':
		OP_12(pcntr)
	elif UC.ROM[pcntr] == '13':
		OP_13(pcntr)
	elif UC.ROM[pcntr] == '14':
		OP_14(pcntr)
	elif UC.ROM[pcntr] == '15':
		OP_15(pcntr)
	elif UC.ROM[pcntr] == '16':
		OP_16(pcntr)
	elif UC.ROM[pcntr] == '17':
		OP_17(pcntr)
	elif UC.ROM[pcntr] == '18':
		OP_18(pcntr)
	elif UC.ROM[pcntr] == '19':
		OP_19(pcntr)
	elif UC.ROM[pcntr] == '1A':
		OP_1A(pcntr)
	elif UC.ROM[pcntr] == '1B':
		OP_1B(pcntr)
	elif UC.ROM[pcntr] == '1C':
		OP_1C(pcntr)
	elif UC.ROM[pcntr] == '1D':
		OP_1D(pcntr)
	elif UC.ROM[pcntr] == '1E':
		OP_1E(pcntr)
	elif UC.ROM[pcntr] == '1F':
		OP_1F(pcntr)

	elif UC.ROM[pcntr] == '20':
		OP_20(pcntr)
	elif UC.ROM[pcntr] == '21':
		OP_21(pcntr)
	elif UC.ROM[pcntr] == '22':
		OP_22(pcntr)
	elif UC.ROM[pcntr] == '23':
		OP_23(pcntr)
	elif UC.ROM[pcntr] == '24':
		OP_24(pcntr)
	elif UC.ROM[pcntr] == '25':
		OP_25(pcntr)
	elif UC.ROM[pcntr] == '26':
		OP_26(pcntr)
	elif UC.ROM[pcntr] == '27':
		OP_27(pcntr)
	elif UC.ROM[pcntr] == '28':
		OP_28(pcntr)
	elif UC.ROM[pcntr] == '29':
		OP_29(pcntr)
	elif UC.ROM[pcntr] == '2A':
		OP_2A(pcntr)
	elif UC.ROM[pcntr] == '2B':
		OP_2B(pcntr)
	elif UC.ROM[pcntr] == '2C':
		OP_2C(pcntr)
	elif UC.ROM[pcntr] == '2D':
		OP_2D(pcntr)
	elif UC.ROM[pcntr] == '2E':
		OP_2E(pcntr)
	elif UC.ROM[pcntr] == '2F':
		OP_2F(pcntr)

	elif UC.ROM[pcntr] == '30':
		OP_30(pcntr)
	elif UC.ROM[pcntr] == '31':
		OP_31(pcntr)
	elif UC.ROM[pcntr] == '32':
		OP_32(pcntr)
	elif UC.ROM[pcntr] == '33':
		OP_33(pcntr)
	elif UC.ROM[pcntr] == '34':
		OP_34(pcntr)
	elif UC.ROM[pcntr] == '35':
		OP_35(pcntr)
	elif UC.ROM[pcntr] == '36':
		OP_36(pcntr)
	elif UC.ROM[pcntr] == '37':
		OP_37(pcntr)
	elif UC.ROM[pcntr] == '38':
		OP_38(pcntr)
	elif UC.ROM[pcntr] == '39':
		OP_39(pcntr)
	elif UC.ROM[pcntr] == '3A':
		OP_3A(pcntr)
	elif UC.ROM[pcntr] == '3B':
		OP_3B(pcntr)
	elif UC.ROM[pcntr] == '3C':
		OP_3C(pcntr)
	elif UC.ROM[pcntr] == '3D':
		OP_3D(pcntr)
	elif UC.ROM[pcntr] == '3E':
		OP_3E(pcntr)
	elif UC.ROM[pcntr] == '3F':
		OP_3F(pcntr)

	elif UC.ROM[pcntr] == '40':
		OP_40(pcntr)
	elif UC.ROM[pcntr] == '41':
		OP_41(pcntr)
	elif UC.ROM[pcntr] == '42':
		OP_42(pcntr)
	elif UC.ROM[pcntr] == '43':
		OP_43(pcntr)
	elif UC.ROM[pcntr] == '44':
		OP_44(pcntr)
	elif UC.ROM[pcntr] == '45':
		OP_45(pcntr)
	elif UC.ROM[pcntr] == '46':
		OP_46(pcntr)
	elif UC.ROM[pcntr] == '47':
		OP_47(pcntr)
	elif UC.ROM[pcntr] == '48':
		OP_48(pcntr)
	elif UC.ROM[pcntr] == '49':
		OP_49(pcntr)
	elif UC.ROM[pcntr] == '4A':
		OP_4A(pcntr)
	elif UC.ROM[pcntr] == '4B':
		OP_4B(pcntr)
	elif UC.ROM[pcntr] == '4C':
		OP_4C(pcntr)
	elif UC.ROM[pcntr] == '4D':
		OP_4D(pcntr)
	elif UC.ROM[pcntr] == '4E':
		OP_4E(pcntr)
	elif UC.ROM[pcntr] == '4F':
		OP_4F(pcntr)

	elif UC.ROM[pcntr] == '50':
		OP_50(pcntr)
	elif UC.ROM[pcntr] == '51':
		OP_51(pcntr)
	elif UC.ROM[pcntr] == '52':
		OP_52(pcntr)
	elif UC.ROM[pcntr] == '53':
		OP_53(pcntr)
	elif UC.ROM[pcntr] == '54':
		OP_54(pcntr)
	elif UC.ROM[pcntr] == '55':
		OP_55(pcntr)
	elif UC.ROM[pcntr] == '56':
		OP_56(pcntr)
	elif UC.ROM[pcntr] == '57':
		OP_57(pcntr)
	elif UC.ROM[pcntr] == '58':
		OP_58(pcntr)
	elif UC.ROM[pcntr] == '59':
		OP_59(pcntr)
	elif UC.ROM[pcntr] == '5A':
		OP_5A(pcntr)
	elif UC.ROM[pcntr] == '5B':
		OP_5B(pcntr)
	elif UC.ROM[pcntr] == '5C':
		OP_5C(pcntr)
	elif UC.ROM[pcntr] == '5D':
		OP_5D(pcntr)
	elif UC.ROM[pcntr] == '5E':
		OP_5E(pcntr)
	elif UC.ROM[pcntr] == '5F':
		OP_5F(pcntr)


	elif UC.ROM[pcntr] == '60':
		OP_60(pcntr)
	elif UC.ROM[pcntr] == '61':
		OP_61(pcntr)
	elif UC.ROM[pcntr] == '62':
		OP_62(pcntr)
	elif UC.ROM[pcntr] == '63':
		OP_63(pcntr)
	elif UC.ROM[pcntr] == '64':
		OP_64(pcntr)
	elif UC.ROM[pcntr] == '65':
		OP_65(pcntr)
	elif UC.ROM[pcntr] == '66':
		OP_66(pcntr)
	elif UC.ROM[pcntr] == '67':
		OP_67(pcntr)
	elif UC.ROM[pcntr] == '68':
		OP_68(pcntr)
	elif UC.ROM[pcntr] == '69':
		OP_69(pcntr)
	elif UC.ROM[pcntr] == '6A':
		OP_6A(pcntr)
	elif UC.ROM[pcntr] == '6B':
		OP_6B(pcntr)
	elif UC.ROM[pcntr] == '6C':
		OP_6C(pcntr)
	elif UC.ROM[pcntr] == '6D':
		OP_6D(pcntr)
	elif UC.ROM[pcntr] == '6E':
		OP_6E(pcntr)
	elif UC.ROM[pcntr] == '6F':
		OP_6F(pcntr)

	elif UC.ROM[pcntr] == '70':
		OP_70(pcntr)
	elif UC.ROM[pcntr] == '71':
		OP_71(pcntr)
	elif UC.ROM[pcntr] == '72':
		OP_72(pcntr)
	elif UC.ROM[pcntr] == '73':
		OP_73(pcntr)
	elif UC.ROM[pcntr] == '74':
		OP_74(pcntr)
	elif UC.ROM[pcntr] == '75':
		OP_75(pcntr)
	elif UC.ROM[pcntr] == '76':
		OP_76(pcntr)
	elif UC.ROM[pcntr] == '77':
		OP_77(pcntr)
	elif UC.ROM[pcntr] == '78':
		OP_78(pcntr)
	elif UC.ROM[pcntr] == '79':
		OP_79(pcntr)
	elif UC.ROM[pcntr] == '7A':
		OP_7A(pcntr)
	elif UC.ROM[pcntr] == '7B':
		OP_7B(pcntr)
	elif UC.ROM[pcntr] == '7C':
		OP_7C(pcntr)
	elif UC.ROM[pcntr] == '7D':
		OP_7D(pcntr)
	elif UC.ROM[pcntr] == '7E':
		OP_7E(pcntr)
	elif UC.ROM[pcntr] == '7F':
		OP_7F(pcntr)
	
	elif UC.ROM[pcntr] == '80':
		OP_80(pcntr)
	elif UC.ROM[pcntr] == '81':
		OP_81(pcntr)
	elif UC.ROM[pcntr] == '82':
		OP_82(pcntr)
	elif UC.ROM[pcntr] == '83':
		OP_83(pcntr)
	elif UC.ROM[pcntr] == '84':
		OP_84(pcntr)
	elif UC.ROM[pcntr] == '85':
		OP_85(pcntr)
	elif UC.ROM[pcntr] == '86':
		OP_86(pcntr)
	elif UC.ROM[pcntr] == '87':
		OP_87(pcntr)
	elif UC.ROM[pcntr] == '88':
		OP_88(pcntr)
	elif UC.ROM[pcntr] == '89':
		OP_89(pcntr)
	elif UC.ROM[pcntr] == '8A':
		OP_8A(pcntr)
	elif UC.ROM[pcntr] == '8B':
		OP_8B(pcntr)
	elif UC.ROM[pcntr] == '8C':
		OP_8C(pcntr)
	elif UC.ROM[pcntr] == '8D':
		OP_8D(pcntr)
	elif UC.ROM[pcntr] == '8E':
		OP_8E(pcntr)
	elif UC.ROM[pcntr] == '8F':
		OP_8F(pcntr)

	elif UC.ROM[pcntr] == '90':
		OP_90(pcntr)
	elif UC.ROM[pcntr] == '91':
		OP_91(pcntr)
	elif UC.ROM[pcntr] == '92':
		OP_92(pcntr)
	elif UC.ROM[pcntr] == '93':
		OP_93(pcntr)
	elif UC.ROM[pcntr] == '94':
		OP_94(pcntr)
	elif UC.ROM[pcntr] == '95':
		OP_95(pcntr)
	elif UC.ROM[pcntr] == '96':
		OP_96(pcntr)
	elif UC.ROM[pcntr] == '97':
		OP_97(pcntr)
	elif UC.ROM[pcntr] == '98':
		OP_98(pcntr)
	elif UC.ROM[pcntr] == '99':
		OP_99(pcntr)
	elif UC.ROM[pcntr] == '9A':
		OP_9A(pcntr)
	elif UC.ROM[pcntr] == '9B':
		OP_9B(pcntr)
	elif UC.ROM[pcntr] == '9C':
		OP_9C(pcntr)
	elif UC.ROM[pcntr] == '9D':
		OP_9D(pcntr)
	elif UC.ROM[pcntr] == '9E':
		OP_9E(pcntr)
	elif UC.ROM[pcntr] == '9F':
		OP_9F(pcntr)
	
	elif UC.ROM[pcntr] == 'A0':
		OP_A0(pcntr)
	elif UC.ROM[pcntr] == 'A1':
		OP_A1(pcntr)
	elif UC.ROM[pcntr] == 'A2':
		OP_A2(pcntr)
	elif UC.ROM[pcntr] == 'A3':
		OP_A3(pcntr)
	elif UC.ROM[pcntr] == 'A4':
		OP_A4(pcntr)
	elif UC.ROM[pcntr] == 'A5':
		OP_A5(pcntr)
	elif UC.ROM[pcntr] == 'A6':
		OP_A6(pcntr)
	elif UC.ROM[pcntr] == 'A7':
		OP_A7(pcntr)
	elif UC.ROM[pcntr] == 'A8':
		OP_A8(pcntr)
	elif UC.ROM[pcntr] == 'A9':
		OP_A9(pcntr)
	elif UC.ROM[pcntr] == 'AA':
		OP_AA(pcntr)
	elif UC.ROM[pcntr] == 'AB':
		OP_AB(pcntr)
	elif UC.ROM[pcntr] == 'AC':
		OP_AC(pcntr)
	elif UC.ROM[pcntr] == 'AD':
		OP_AD(pcntr)
	elif UC.ROM[pcntr] == 'AE':
		OP_AE(pcntr)
	elif UC.ROM[pcntr] == 'AF':
		OP_AF(pcntr)

	elif UC.ROM[pcntr] == 'B0':
		OP_B0(pcntr)
	elif UC.ROM[pcntr] == 'B1':
		OP_B1(pcntr)
	elif UC.ROM[pcntr] == 'B2':
		OP_B2(pcntr)
	elif UC.ROM[pcntr] == 'B3':
		OP_B3(pcntr)
	elif UC.ROM[pcntr] == 'B4':
		OP_B4(pcntr)
	elif UC.ROM[pcntr] == 'B5':
		OP_B5(pcntr)
	elif UC.ROM[pcntr] == 'B6':
		OP_B6(pcntr)
	elif UC.ROM[pcntr] == 'B7':
		OP_B7(pcntr)
	elif UC.ROM[pcntr] == 'B8':
		OP_B8(pcntr)
	elif UC.ROM[pcntr] == 'B9':
		OP_B9(pcntr)
	elif UC.ROM[pcntr] == 'BA':
		OP_BA(pcntr)
	elif UC.ROM[pcntr] == 'BB':
		OP_BB(pcntr)
	elif UC.ROM[pcntr] == 'BC':
		OP_BC(pcntr)
	elif UC.ROM[pcntr] == 'BD':
		OP_BD(pcntr)
	elif UC.ROM[pcntr] == 'BE':
		OP_BE(pcntr)
	elif UC.ROM[pcntr] == 'BF':
		OP_BF(pcntr)

	elif UC.ROM[pcntr] == 'C0':
		OP_C0(pcntr)
	elif UC.ROM[pcntr] == 'C1':
		OP_C1(pcntr)
	elif UC.ROM[pcntr] == 'C2':
		OP_C2(pcntr)
	elif UC.ROM[pcntr] == 'C3':
		OP_C3(pcntr)
	elif UC.ROM[pcntr] == 'C4':
		OP_C4(pcntr)
	elif UC.ROM[pcntr] == 'C5':
		OP_C5(pcntr)
	elif UC.ROM[pcntr] == 'C6':
		OP_C6(pcntr)
	elif UC.ROM[pcntr] == 'C7':
		OP_C7(pcntr)
	elif UC.ROM[pcntr] == 'C8':
		OP_C8(pcntr)
	elif UC.ROM[pcntr] == 'C9':
		OP_C9(pcntr)
	elif UC.ROM[pcntr] == 'CA':
		OP_CA(pcntr)
	elif UC.ROM[pcntr] == 'CB':
		OP_CB(pcntr)
	elif UC.ROM[pcntr] == 'CC':
		OP_CC(pcntr)
	elif UC.ROM[pcntr] == 'CD':
		OP_CD(pcntr)
	elif UC.ROM[pcntr] == 'CE':
		OP_CE(pcntr)
	elif UC.ROM[pcntr] == 'CF':
		OP_CF(pcntr)

	elif UC.ROM[pcntr] == 'D0':
		OP_D0(pcntr)
	elif UC.ROM[pcntr] == 'D1':
		OP_D1(pcntr)
	elif UC.ROM[pcntr] == 'D2':
		OP_D2(pcntr)
	elif UC.ROM[pcntr] == 'D3':
		OP_D3(pcntr)
	elif UC.ROM[pcntr] == 'D4':
		OP_D4(pcntr)
	elif UC.ROM[pcntr] == 'D5':
		OP_D5(pcntr)
	elif UC.ROM[pcntr] == 'D6':
		OP_D6(pcntr)
	elif UC.ROM[pcntr] == 'D7':
		OP_D7(pcntr)
	elif UC.ROM[pcntr] == 'D8':
		OP_D8(pcntr)
	elif UC.ROM[pcntr] == 'D9':
		OP_D9(pcntr)
	elif UC.ROM[pcntr] == 'DA':
		OP_DA(pcntr)
	elif UC.ROM[pcntr] == 'DB':
		OP_DB(pcntr)
	elif UC.ROM[pcntr] == 'DC':
		OP_DC(pcntr)
	elif UC.ROM[pcntr] == 'DD':
		OP_DD(pcntr)
	elif UC.ROM[pcntr] == 'DE':
		OP_DE(pcntr)
	elif UC.ROM[pcntr] == 'DF':
		OP_DF(pcntr)

	elif UC.ROM[pcntr] == 'E0':
		OP_E0(pcntr)
	elif UC.ROM[pcntr] == 'E1':
		OP_E1(pcntr)
	elif UC.ROM[pcntr] == 'E2':
		OP_E2(pcntr)
	elif UC.ROM[pcntr] == 'E3':
		OP_E3(pcntr)
	elif UC.ROM[pcntr] == 'E4':
		OP_E4(pcntr)
	elif UC.ROM[pcntr] == 'E5':
		OP_E5(pcntr)
	elif UC.ROM[pcntr] == 'E6':
		OP_E6(pcntr)
	elif UC.ROM[pcntr] == 'E7':
		OP_E7(pcntr)
	elif UC.ROM[pcntr] == 'E8':
		OP_E8(pcntr)
	elif UC.ROM[pcntr] == 'E9':
		OP_E9(pcntr)
	elif UC.ROM[pcntr] == 'EA':
		OP_EA(pcntr)
	elif UC.ROM[pcntr] == 'EB':
		OP_EB(pcntr)
	elif UC.ROM[pcntr] == 'EC':
		OP_EC(pcntr)
	elif UC.ROM[pcntr] == 'ED':
		OP_ED(pcntr)
	elif UC.ROM[pcntr] == 'EE':
		OP_EE(pcntr)
	elif UC.ROM[pcntr] == 'EF':
		OP_EF(pcntr)

	elif UC.ROM[pcntr] == 'F0':
		OP_F0(pcntr)
	elif UC.ROM[pcntr] == 'F1':
		OP_F1(pcntr)
	elif UC.ROM[pcntr] == 'F2':
		OP_F2(pcntr)
	elif UC.ROM[pcntr] == 'F3':
		OP_F3(pcntr)
	elif UC.ROM[pcntr] == 'F4':
		OP_F4(pcntr)
	elif UC.ROM[pcntr] == 'F5':
		OP_F5(pcntr)
	elif UC.ROM[pcntr] == 'F6':
		OP_F6(pcntr)
	elif UC.ROM[pcntr] == 'F7':
		OP_F7(pcntr)
	elif UC.ROM[pcntr] == 'F8':
		OP_F8(pcntr)
	elif UC.ROM[pcntr] == 'F9':
		OP_F9(pcntr)
	elif UC.ROM[pcntr] == 'FA':
		OP_FA(pcntr)
	elif UC.ROM[pcntr] == 'FB':
		OP_FB(pcntr)
	elif UC.ROM[pcntr] == 'FC':
		OP_FC(pcntr)
	elif UC.ROM[pcntr] == 'FD':
		OP_FD(pcntr)
	elif UC.ROM[pcntr] == 'FE':
		OP_FE(pcntr)
	elif UC.ROM[pcntr] == 'FF':
		OP_FF(pcntr)











		

