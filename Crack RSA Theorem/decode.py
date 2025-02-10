from sympy import Integer, mod_inverse  # Thư viện SymPy hỗ trợ số học nguyên lớn
from Cryptodome.Util.number import long_to_bytes  # Chuyển đổi số nguyên lớn thành chuỗi bytes
import gmpy2  # Thư viện hỗ trợ tính toán số nguyên lớn hiệu quả


def chinese_remainder_theorem(c, n):
    """
    Giải hệ phương trình đồng dư sử dụng Định lý phần dư Trung Hoa (CRT).
    - c: danh sách các ciphertext tương ứng với mỗi modulus
    - n: danh sách các modulus (mẫu số)

    Trả về: Giá trị kết hợp từ các đồng dư modulo N.
    """
    N = Integer(n[0] * n[1] * n[2])  # Tính tích của tất cả các modulus
    result = 0  # Khởi tạo biến tổng hợp giá trị

    for i in range(3):
        Ni = N // n[i]  # Tính Ni = N / ni (phần còn lại sau khi bỏ mẫu số hiện tại)
        Mi = mod_inverse(Ni, n[i])  # Tính nghịch đảo modulo của Ni với ni
        result += c[i] * Ni * Mi  # Cộng dồn giá trị theo CRT

    return result % N  # Trả về giá trị sau khi lấy modulo N


# Danh sách các giá trị modulus (n) và ciphertext (c) đã cho
n = [
    17207265790882646794094060699396252304792863634408709467064448136019010109025997020898314483385637078359719528162591357510693214040370777440541205718488664397262466510161570689475068365333826268090531991662587125379731104413305693688346795879277830072304851441541619451086903472522829440453555903550938007436560750610230200740503479003512186077934802147871071466003074494441387116811438831294201289775705545106668964413807619616529230468882304573084599449864126298205354000680908276872773877920410719473594604121729408518968810381222602442411264300381493449585193880196033358411837352512524707379056349426306512578621,
    15831433912089650838232056168560013122852640882095636644920264428253688685155266103547661956117477467616304169200449400836686850354890335224353351294256729117974095055350639469624117094883657019163841924729962832257210733487747837397522982625458691005378077932757546078306200113632369771801868621414127398153248205740680907840799735814952060697950138529588568505575708877335193714718720548744775070489187574869150656629750080291288831066797603475455333634970408933455732242575945963812966064474578594130432381088719359550404072321621355381063870400331903472387522694532510385579904942353031601127936148519655210272787,
    21403999901619771063723669644286281595233876075398497681843535476733127115701027464847013704688642739690273597027257939958386909778544384304590551741691479934502276026253648191333278314205153198518591534746087070362075687387658312750543643826515402704757876967324722620296891813791471563066631614121057583188213048179722327228352453333793736174327685007214605298201419868547770062737267472157223217397190648351380844368290780929427713606801594306049709154303268858351688549855796775039055033576202799446981924629873685011910813066823219483601671739530712384073546524066449042192306837596223620132014477918438081208853
]
c = [
    8698412614484158642136320299278169344584715978606155329005425573344852461994276501554671172505454668201041387165722669890015345082907827244307043312033283214201290559369756842463865033470892436752306922590773771531074087322141999746403678547109289932708773268179436420952606399036062492136979478383751867139926825698853017101290463043707333735673936770035820662931702612071850725773255532375325195605946216076804799058009911399261047142591549704476675630073241289631680200024068915895048925401633216798881221594442362603325996600887974237489019399893734757995494010713131326973641504877651149922630617226480743975939,
    1065403436384187677033799128553394010960358379544673492381286113796657373659156517035730783384768288467235318398038736702888207435236951311703880348656976080403494641385700091306429917016434148302965027221399581282284730191216358585146498931470917159530952630193631228745226610293317119255257586876848560366321020101246126091137495513933645948915261506913758513003544662704877766331207304462948699709549387119845411594951246897608655760753690423138386638306966900546403527173092031456900412764125411635183887104337414054736336182885971973917089255993031266635004514625504308885321517141061771738006102953209152743333,
    4932255772525268967345482362916025713656578140477940173581415596506037545262633697271455757345130422272172963855138918809952781387711266260189942554168372200617003736624529745760652852497464117697377123108758638815225793972886344044437278428023602629322684487913522674926139913754335568622235003036853607227867835264983083851551037853571951269256022569751906632427377131592215448497512098091592968078113201871561385853648653103116819662881751428693426757555214763575414778299035447571553263998704186142007986354373828781249200878184350148748154251228549182164696290840760753373906836887229474007313381691194116644400
]

# Giải bài toán đồng dư bằng CRT
y_cubed = int(chinese_remainder_theorem(c, n))  # Chuyển kết quả về kiểu int

# Tìm căn bậc ba của y_cubed
y, exact = gmpy2.iroot(int(y_cubed), 3)

# Kiểm tra xem căn bậc ba có chính xác không
if not exact:
    print("Warning: Cube root approximation may not be exact.")

# Chuyển số nguyên y thành chuỗi bytes rồi giải mã thành chuỗi ký tự
try:
    flag = long_to_bytes(int(y)).rstrip(b'\x00').decode(errors='ignore')
    print("Recovered flag:", flag)
except Exception as e:
    print("Decoding error:", e)
