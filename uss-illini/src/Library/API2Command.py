# %load API2Command
'''
Quick 1-Stop Update DB

Main Methods:
    insertDB(account_ids,ship_ids,module_ids,clan_ids)
    ------------>pass in [] in the field if no update should be made<-------------

    list("") = example_account_ids #ericsama, Quincy0v0
    list("") = example_ship_ids #all non-gold ships id
    list("") = example_module_ids #all shima's module
    list("") = example_clan_ids #kuma, seal
'''
import InsertCommand
import Ship_idDict
import API2Python as a2p

def insertDB(account_ids,ship_ids,module_ids,clan_ids):
    result = ""
    for account_id in account_ids:
        result += InsertCommand.insert_account_stats(account_id)
        result += InsertCommand.insert_rank_ship_stats(account_id)
        result += InsertCommand.insert_rank_account_stats(account_id)
        for ship_id in ship_ids:
            result += InsertCommand.insert_random_ships_stats(account_id,ship_id)
    for module_id in module_ids:
        result += InsertCommand.insert_module(module_id)
    for ship_id in ship_ids:
        result += InsertCommand.insert_ship(ship_id)
    for clan_id in clan_ids:
        result += InsertCommand.insert_clan(clan_id)
    return result

example_account_ids = ["1011528019","1019218342"]
kuma_account_ids = ["1003333910","1004477726","1007175219","1008316697","1008625506",'1009061145','1009661450','1010209482','1010323946','1010724543','1011528019','1013304000','1013334385','1013587959','1013999547','1014471821','1015329727','1015357346','1015493067','1015610394','1016120451','1018349928','1021128077','1021170377','1021760124','1021825753','1021838805','1023915822','1024488643','1024492045','1025871171','1026265082','1026478590','1027962043','1028085712','1029202697','1029258263','1030351561','1030590838','1031599654']
all_ship_ids = [Ship_idDict.ship_id_dict[nation][ship_type][tier][ship] for nation in Ship_idDict.ship_id_dict.keys() for ship_type in Ship_idDict.ship_id_dict[nation].keys() for tier in Ship_idDict.ship_id_dict[nation][ship_type].keys() for ship in Ship_idDict.ship_id_dict[nation][ship_type][tier].keys()]
all_module_ids = list(set([module_id for ship_id in all_ship_ids for module_id in a2p.get_ship_encyclopedia(a2p.application_id,ship_id)[44].keys()]))
all_module_ids_fast = ['3423449072', '3442913232', '3423350768', '3350179024', '3558584304', '3440783056', '3348508464', '3453988816', '3444551632', '3979325424', '3340611408', '3559796432', '4178325200', '3554029264', '4072058576', '3350179632', '3849727440', '3968708432', '4293668688', '3422302192', '3554422480', '4061573072', '4082905040', '4157451984', '3433836528', '3554422768', '3978702288', '3549278000', '3967561712', '3453988656', '3453890256', '3873287984', '3925618384', '3642142416', '3538693840', '4291800784', '3444420048', '3317673680', '3549179856', '3318722256', '3968839664', '3442880208', '3663114192', '3768430384', '3822039024', '3874336464', '3979194064', '3851169232', '3538792400', '3979194352', '3552980688', '3338055120', '3977654224', '3454414640', '3451301872', '3761090384', '3664129744', '3664752464', '3761647312', '3549179728', '3747360592', '3874467024', '3758993104', '3758534640', '4052725456', '3455004656', '3967200720', '3454808016', '4083003088', '3442913264', '4293898192', '3447107280', '4292259280', '3556749008', '3967561680', '3978047312', '3766464304', '3758993392', '4083560400', '3769577168', '3747590128', '3538694128', '3348508112', '3662032688', '3863752400', '3441405392', '4061933008', '3843010256', '4188450608', '4073467888', '4188811088', '3873877200', '3349917392', '3768429776', '3842420432', '3978014704', '3348967120', '3873189680', '4293668048', '3453365712', '3659935440', '3455036624', '3874467664', '3978276656', '4062621648', '3663572688', '3767938864', '3767283696', '3558616880', '3538693584', '3872796624', '3454939120', '3975556912', '3443273520', '3768463056', '3767381712', '4155944400', '3339104240', '3557797584', '3863818224', '3744214736', '3342216912', '3548131312', '3443961808', '3979096016', '3863392080', '4187402224', '3652988368', '3862343472', '3454446800', '3453824720', '3937382096', '3662491344', '3764793296', '3507236560', '4083133904', '3452317488', '3662425904', '3865030480', '3550457680', '4083592400', '3423350480', '3555110896', '3630608080', '4293308240', '3422400496', '3559632880', '3873157104', '4081496016', '4073467856', '3347853264', '4082904784', '4189040464', '3557567696', '3756404176', '3872829264', '3449204720', '3966512848', '3977686832', '3558813680', '3769577456', '3655315280', '3558617040', '3349556432', '3538923216', '3452350448', '3452710704', '4073565648', '3537874384', '4073074640', '3660984112', '3329208016', '3871092688', '3452350256', '4073697232', '3505139408', '3350047952', '3758894928', '3841732592', '3758534096', '3736973296', '3735924720', '3978735440', '3348901680', '3924569808', '3663474640', '4081463280', '3443928784', '3874335952', '3968610000', '3551932112', '3766889680', '3632017392', '4061572816', '3454807888', '4292259536', '4081495856', '3558682320', '4073467696', '3862704112', '3862802384', '3339464528', '3350146768', '3450613744', '3347492560', '4083953456', '4186320880', '3662524368', '3979096048', '3851267536', '3559272272', '3936759248', '3766235120', '3769511920', '3537743824', '3968610288', '3977686736', '3979063280', '4189040432', '3977654256', '4073107440', '3769347792', '4062981584', '3558223824', '3339693776', '3873844432', '3633295344', '4292259024', '3611143888', '3632017104', '4185665328', '3967561520', '3650530768', '3336548144', '3536203216', '3349557200', '3559894992', '3758993360', '3556617936', '4188450768', '3556159472', '3652988752', '4080905936', '3978178544', '3660328944', '3760041808', '3558256432', '3957174256', '4072058672', '3444420304', '4062031824', '3653677040', '4072419120', '4083593040', '4188450640', '3852906480', '3443961648', '4083593008', '3663081264', '3766234576', '3344314064', '3421482704', '3631656656', '4166790608', '3659280368', '3871747792', '3862703952', '3349950448', '3455037264', '3664620752', '3348082640', '3757486064', '3769610032', '3664523216', '3451301680', '3863752496', '3556519728', '3433475792', '3443273712', '3444551472', '3619434192', '3453857776', '3339693520', '3447467472', '3444321744', '4293898064', '3453857584', '4083593200', '3768430032', '3432427216', '3642503120', '4083560240', '3454414544', '3979194160', '3632705520', '3536825808', '3550326608', '3872829424', '3548229424', '3642109648', '3861655344', '3663114032', '3768332080', '3978735056', '3976998704', '3664752080', '4185272016', '3651579344', '4188418000', '3874238448', '3329076944', '3663081168', '3663081424', '3969757008', '3862802224', '4187402032', '4188811248', '3454774992', '3661376976', '3559665456', '3937251312', '3767512880', '3873877808', '3758993200', '3979095504', '3557666608', '4083134416', '3559272144', '3443928528', '3763318768', '3537874640', '3451301584', '4082544592', '3507334864', '4177276624', '3663081456', '3448122832', '3862343504', '3757944624', '4082904912', '3763187696', '3652988912', '3958353904', '4082544432', '3443273680', '3308105424', '3559763952', '3339464144', '3348868816', '3874434768', '4062621680', '4188909552', '3654266864', '3442913072', '3863392048', '4187762672', '3767971632', '3976998864', '4061933264', '3725340656', '3453759280', '3643781072', '3862704080', '3350048720', '3453398224', '4061573104', '3736514544', '3874205392', '3454938832', '4072058704', '4084051152', '4293766960', '3871092528', '3664523088', '3968610096', '3763089392', '4083134448', '3549278032', '3453890544', '4073107280', '3874238288', '4084051792', '3768331472', '3630968528', '3660328656', '3558584016', '3449565168', '3350081232', '3766234928', '4082904880', '3555471344', '3851398608', '4061572560', '3643551696', '3559305168', '3768987600', '3664490192', '3746312176', '3631656944', '3346444272', '3559665488', '3747000272', '3664129872', '3654266672', '3347034064', '3726388944', '3873877968', '3444551664', '3664162640', '3767282896', '4062031856', '3538693936', '3979193808', '3349131056', '3725340368', '3832295120', '3863392208', '3766923056', '4186943280', '3874336720', '3454414672', '3977686224', '3553374192', '4083134256', '3556519888', '3832524240', '3348901328', '3748048848', '3747000144', '3349000176', '3349557072', '3339562800', '3968249808', '3444420432', '3758993232', '3443371824', '3450253296', '3453398480', '4084182832', '3978702544', '3967659824', '3412864720', '3559763920', '3641454576', '4187992016', '3873189072', '3553013744', '4073696720', '3641454288', '3622678224', '3453398992', '3767939024', '4167478736', '4062982128', '3318591184', '4186353456', '3978047280', '3662425552', '3978145488', '3350179280', '3968708048', '3442913104', '3748507600', '3664621392', '4292259664', '4073566160', '3347853296', '3455037392', '3768299216', '3978735408', '3978046928', '3653087216', '3978735312', '3453366224', '3661377232', '3421253616', '4084183024', '3863392240', '3557208016', '3830198256', '3978047472', '3758992848', '3558616912', '3978702672', '3757485776', '3759124464', '3409358544', '3559730896', '3873419056', '3840683728', '3654036944', '3453759184', '3958222832', '4166430416', '3558223856', '3768299504', '3345854448', '3350048560', '4187402192', '3453398864', '3766234832', '3664654320', '3556618224', '3538333488', '3978047440', '3633163984', '3349000144', '3454906192', '3759124304', '3642502864', '3661017072', '3850120656', '3653087024', '3663572432', '4292259824', '3411816144', '3559305008', '3642503152', '3517820912', '3643650000', '3979193552', '3748048592', '3643158224', '3549409264', '3662655440', '4167478992', '3863850960', '3747000016', '3757846352', '4083559632', '3348999632', '3654135632', '3978243792', '3559862256', '3658919920', '3977096912', '4291210960', '4062982096', '3652628304', '3967561168', '4178554576', '3659968496', '3348901584', '3863850992', '3968708560', '3517951984', '4187762512', '3339464400', '3548819408', '3767513072', '3724521168', '4188417232', '3556519632', '3662524112', '3339562704', '3547770704', '4073107408', '3444420592', '3328618192', '3758534480', '3967200976', '3443503056', '3559271632', '3978014416', '3549179888', '3769446096', '3735924432', '3432427504', '3756436944', '3862343376', '3338644944', '3664751824', '3454414832', '3643191248', '3621531344', '3454807856', '3979095760', '3350179792', '3549278160', '3747360720', '3452710896', '3850776016', '3968249552', '3872239568', '3664130000', '3653676880', '4073566032', '3350048752', '3443371984', '4188450800', '3967201232', '3757485904', '3976638416', '3558846288', '3978276816', '3758534608', '4072419280', '4292849104', '3864899408', '3664752592', '3874467824', '3548819152', '4188417488', '3747459024', '4188909520', '3432787952', '3453365968', '3422531280', '4188811056', '4187991856', '3432787664', '4293308400', '3662032336', '3768397520', '4063080144', '3438685904', '4052594672', '3348541232', '3557567952', '4168068560', '3967561424', '3967201072', '4084182864', '3454414032', '3945541616', '3758960624', '3956715504', '4293307856', '3967201264', '4186714064', '4073107152', '3536596688', '3349032656', '4082511664', '4293767120', '4187860784', '3442912976', '4073566000', '3454447408', '3976605680', '3664752432', '3453759440', '3652628272', '4083953488', '4063080432', '3621760720', '4084051952', '3444322096', '4293766992', '3979161296', '3558845648', '3862802416', '3455036880', '3620482768', '3979194320', '3663703856', '3652988720', '3453398832', '4293898032', '3664654032', '3871780560', '3434065360', '3765284848', '4072058832', '3411455696', '3434065904', '3874467536', '3433836240', '3339104048', '4178325488', '3664490480', '4084051760', '3557666256', '4084182480', '3452317648', '3748409296', '3454414800', '3662655472', '3766235088', '3553373904', '3642601424', '3643190992', '3556749296', '3765874480', '3328978640', '4073697264', '3975950128', '3664130032', '3737563120', '3349557232', '4073467728', '4157582800', '3422990032', '3663539920', '3871780656', '3979325264', '3968708304', '3768560848', '4187761872', '3872829392', '3548131024', '3759550160', '3549179600', '4177276912', '3748638672', '4167839184', '3349950288', '3873845072', '3412504272', '3557699568', '3767971024', '3643551440', '3538333136', '3655184208', '4186320592', '3664621360', '3967791088', '4082904272', '3874467632', '3659378672', '3769020208', '3537284912', '3661377520', '3450843120', '3339103696', '4156992976', '3765186352', '3757486032', '3558846416', '3445469008', '3766923216', '3451301840', '3747360752', '3759124272', '3451662128', '3654037296', '4072419312', '3759124176', '3558813392', '3654037200', '3765841872', '3967659984', '4080414416', '3536596784', '3318722544', '3871321808', '4083003184', '3872828624', '3347459536', '3766922448', '3979062992', '3870044144', '3556159440', '3758534352', '3841371856', '4072418768', '3978702800', '4187401424', '4187369456', '3349949904', '3622579920', '3557568464', '3559272400', '3863981872', '3968249680', '3347459888', '3968839632', '3642142672', '3552325616', '3558715088', '4074614608', '3872829136', '3769348080', '3538791888', '3664719568', '3747589584', '3979325232', '3339562448', '3556519376', '3664621520', '4073565904', '3842780880', '3559894864', '4073696976', '3979227120', '3979324880', '3663474480', '3610095312', '3339103952', '3348082672', '3758501872', '3451760080', '3662065648', '3350179664', '3768987440', '3444322128', '3454447440', '3554422224', '3660328912', '3745263312', '3443273424', '3664162000', '3527814608', '3968249840', '4072517424', '3968610128', '3348508656', '4081856304', '3958124240', '3664523056', '3664719856', '3451760624', '4187369264', '3957763792', '3874336592', '4062981840', '4073467600', '3660427248', '3767283504', '3538333392', '3863752688', '3447074256', '3533057488', '3547770832', '3454447568', '3873386192', '3831246288', '3663572976', '3873189584', '3977687024', '3870732080', '3659968464', '3870044112', '3526799344', '3873845232', '3767513040', '3841961680', '3348901840', '3769478960', '3861294544', '3926896336', '3554062320', '3766923248', '3978735600', '3873287888', '4052135920', '3349589968', '3767348944', '3654135792', '4083003344', '4082511568', '3769479152', '3760631504', '4283182544', '3873189840', '3979095888', '3347034096', '3340742480', '3863850832', '3439734480', '3348508368', '3968708592', '3979095248', '3663474512', '3537645008', '3663080656', '3977686864', '3978145584', '3455004368', '3643551728', '3872108528', '3874369520', '3664522704', '3558714832', '4156304848', '4186353616', '4293308368', '4072419152', '3664588496', '4292259632', '3734875856', '4080447280', '3549409072', '3452809168', '3555471056', '4051447504', '3872239600', '3869683664', '3653676848', '3452350160', '3721375440', '3347492816', '3559632592', '3968839472', '3448155856', '3454906320', '3451269104', '3738152656', '3559665616', '3663441616', '3755388368', '3870732240', '3506187984', '3445600080', '3318493168', '3755355600', '3872141104', '3433934544', '3736874704', '3433476080', '3768430288', '3977653456', '3757846320', '4189040592', '3976605488', '4291571408', '3349131216', '3452710864', '3652628464', '3862343632', '3979292368', '3349557040', '3443404784', '3757845968', '3979325392', '3661377328', '3664129840', '3546721744', '3632705232', '3762040816', '4293897424', '3544624592', '3349950256', '3559861968', '3558747856', '3874435056', '4082544624', '3758895056', '3874467792', '3558256464', '4073107248', '4157451728', '3526111216', '3337596720', '4292259792', '3451891152', '3346411216', '3863981776', '3863850704', '4082511856', '3557207856', '3538923312', '3832294864', '3557633744', '3547770576', '3873189872', '4080807728', '3652627920', '3759582928', '3758894544', '3853364944', '3757846480', '4084051408', '3549408976', '3437669840', '4292718288', '3545673168', '4188417840', '3975589680', '4189039824', '3873419248', '3870731984', '3558714576', '3978702032', '3978244080', '3831934416', '3350048208', '3968839376', '4167937488', '3874205680', '4157353424', '3831246832', '3873418960', '3748409168', '3737923280', '3760598736', '3630968816', '3537645360', '3769511632', '4185665488', '3968708400', '3349589456', '3349556944', '3633295056', '4063211216', '3956715216', '3548819440', '3978702832', '3863752656', '3748507344', '3757846224', '4072058864', '3443961680', '4186812400', '3957764080', '3978702640', '4072058320', '3558256592', '3654135600', '3436621264', '3874238416', '3557568304', '4293668656', '4083953648', '3345362640', '3554652144', '3339464688', '3853266928', '4293767152', '3349950416', '3726389232', '3654135248', '4063211504', '3559305040', '3432885968', '3444387824', '3348508624', '3433017136', '3661016880', '3664162768', '3444322288', '3975950288', '3830885840', '3976998896', '3443961296', '3453759312', '3957075664', '3555569648', '3658231792', '3347918544', '3547770320', '3842781168', '3451662320', '3831901648', '3663572784', '3442224592', '4082544464', '4074745680', '3958124528', '3957075952', '4189040624', '3443502800', '3663473872', '3454775280', '3620712144', '3453726416', '3348999984', '3968839120', '3454807248', '3874238256', '3444420400', '3872239312', '4187762640', '3654037328', '3350179824', '3349098192', '3556126512', '3663474128', '3757485520', '3453758672', '4084182224', '3873844944', '3758534448', '3454414288', '3559272432', '4187402064', '3453365456', '3979292656', '4293766352', '3832393168', '3339464496', '4187992048', '3559763760', '3448516048', '3557175248', '3548819280', '3872795856', '3441831632', '3451662288', '3968610256', '3318492880', '3548131152', '3663114064', '3870273232', '3863752528', '3977654064', '3978734800', '4083952848', '3536596976', '4293668816', '3664162608', '3550883536', '3853365232', '3860245968', '4187368912', '3601247952', '3862703920', '3863850800', '3757453008', '3653643728', '3662065456', '3872370640', '4061933552', '3555470800', '4293308208', '3558255824', '3874336560', '3527159792', '4061933520', '3546263344', '3873877712', '3410865872', '4283280848', '3452350416', '3759026160', '3873255120', '3769609680', '3873156816', '3318132720', '3830197968', '3861655248', '3453366064', '3558748144', '3766890288', '3661377488', '3978735568', '3769380656', '3967561552', '3663605456', '3978276848', '4178423504', '3654037488', '4052135632', '3872796464', '3968249648', '3534106064', '4083559888', '3341168336', '3968249296', '3863982032', '3555569360', '4082543824', '3549245424', '3766890192', '3454906160', '3873878000', '3872796368', '4187762480', '4188909360', '3443273168', '3768987632', '3454873296', '3653676496', '3549277904', '3443961840', '3975589840', '4063211472', '3434065616', '4073697072', '3768987472', '3874336752', '3977653968', '3549408720', '3759124432', '3761680080', '3968609744', '4062621392', '3410767568', '3978047184', '3422301904', '3547311920', '3874237648', '3452940272', '4082905072', '3926765264', '3664129232', '3629559504', '3443273552', '3869650640', '3409718992', '3349589808', '3874303696', '3556159280', '3957730768', '3660983760', '3349949648', '3871747888', '3762728656', '4293668848', '3549278192', '3549409232', '3874238160', '3661475824', '4083592912', '3947638768', '3452809200', '3765874640', '3410407120', '3537645552', '3978276304', '3346410960', '3556125904', '3968675824', '3873189712', '3548262384', '3757485872', '4052496080', '3765841104', '3527847920', '3658886864', '4292849648', '3976638256', '3841732304', '3442912720', '3660558320', '3873877840', '3978046672', '3350015696', '3557666512', '4072419024', '3654103024', '3535777232', '4157583344', '3871748080', '3870699472', '3748048720', '3558616272', '3454447056', '3349589840', '3421253328', '4186713904', '3659935696', '3347951600', '3852218352', '3976605392', '3423448784', '3762728944', '3727437520', '3976605648', '3873845200', '3455037232', '3863982064', '3350048592', '4188909392', '3548786480', '4073467344', '4062621136', '3349589712', '3548131280', '3557207248', '3661017040', '3663113424', '4188810448', '4051087344', '3969888080', '3557175088', '3444322256', '3664522448', '3349590000', '3851857904', '3767283664', '3516772336', '3767381968', '3444420560', '3977686480', '3870142160', '4188811216', '3654266576', '3979095856', '3977686992', '3748015568', '3547770864', '3559763792', '4083560272', '3349589200', '4185304880', '3537645264', '4081856464', '3765874672', '3444322000', '3434065712', '3454905808', '3307056848', '3758894800', '3979324624', '3863391952', '3653217744', '3537284560', '4083953360', '3748409328', '3339104080', '4188450000', '3453955792', '4293307600', '3767283152', '3761680368', '3979194192', '3767283408', '4189040336', '3758894896', '3652988624', '3872829232', '3873845040', '3347951568', '3874369232', '4187860944', '3760172880', '3967201104', '3454905552', '3348541392', '3411914448', '3452776144', '4185305040', '4188908752', '3663441904', '3978145744', '4073106896', '3831246544', '4063080400']
example_clan_ids = ["1000043952","1000044201"]
