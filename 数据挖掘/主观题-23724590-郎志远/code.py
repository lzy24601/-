def calculate_relative_time(data_dict): 
    """ 计算相对时间的字典，包含两个键 time1 和 time2，值是列表，分别计算
    为：
    time1 = '发病到首次影像检查时间间隔' + '随访 1 时间点' - '入院首次检查时
    间点' time2 = '发病到首次影像检查时间间隔' + '随访 2 时间点' - '入院首次检查时
    间点' Args:
    data_dict (dict): 包含数据的字典
    Returns:
    dict: 包含两个键 time1 和 time2 的相对时间字典
    """
    time1_values = [data_dict['发病到首次影像检查时间间隔'][i] + ((
    data_dict[' 随 访 1 时 间 点 '][i] - data_dict[' 入 院 首 次 检 查 时 间 点'][i]).total_seconds() / 3600) for i in range(len(data_dict['发病到首次影像检查时间间隔']))]
    time2_values = [data_dict['发病到首次影像检查时间间隔'][i] + ((data_dict['随访 2 时间点'][i] - data_dict['入院首次检查时间点'][i]).total_seconds() / 3600) for i in range(len(data_dict['发病到首次影像检查时间间隔']))]
    relative_time_dict = {
    'time1': time1_values,
    'time2': time2_values
    }
    return relative_time_dict
def is_volume_increase(previous_volume, current_volume): 
    """ 判断体积是否增大的函数。
    Args:
    previous_volume (float): 上一次的体积
    current_volume (float): 当前的体积
    Returns:
    bool: 如果下一次的体积比上一次增加 6 或以上，或者相对体积增加≥
    33%，返回 True；否则返回 False
    """ 
    volume_increase = current_volume - previous_volume
    # 计算相对体积增加百分比
    relative_increase = (volume_increase / previous_volume) * 100 if
    previous_volume != 0 else 0
    # 检查条件
    if volume_increase >= 6 or relative_increase >= 33:
        return True
    else:return False
    #判断某个时间点是否在 48 小时内且发生血肿
    def is_volume_increase_within_time(time,is_volume_increase):
        if time<=48 and is_volume_increase==True:return True
        else:return False

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.softmax = nn.Softmax(dim=1)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)
        init.xavier_normal_(self.fc1.weight)
        init.xavier_normal_(self.fc2.weight)
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.softmax(x)
        return x
def normalize(data, index):
    column_to_normalize = index
    # 计算列的最小值和最大值
    min_val = data[:, column_to_normalize].min()
    max_val = data[:, column_to_normalize].max()
    # 执行 Min-Max 归一化
    normalized_column = (data[:, column_to_normalize] - min_val) / (max_val - min_val)
    # 将归一化后的列替换回原数组
    data[:, column_to_normalize] = normalized_column
    return data
def show_residual(pre_y, y):
    residuals = y - pre_y
    sse = np.sum(residuals ** 2)
    mean_actual = np.mean(y)
    tss = np.sum((y - mean_actual) ** 2)
    r_square = 1 - (sse / tss)
    mean_residual = np.mean(residuals)
    std_residual = np.std(residuals)
    plt.scatter(y, residuals)
    plt.xlabel("Actual Values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    plt.axhline(y=0, color='r', linestyle='--')
    plt.show()
    print(f"平均残差: {mean_residual}")
    print(f"标准差: {std_residual}")
    print("SSE:", sse)
    print("R-square:", r_square)
def merge_data(CheckNumInfos):
    CheckNumInfos = sorted(CheckNumInfos, key=lambda x: x.relative_time)
    tmps = []
    ks = CheckNumInfos[0].k
    cnt = 1
    for i in range(1, len(CheckNumInfos)):
    if CheckNumInfos[i].relative_time == CheckNumInfos[i - 1].relative_time:
        cnt += 1
        ks += CheckNumInfos[i].k
    else:
        tmps.append(CheckNumInfo(-1, -1, CheckNumInfos[i - 1].check_time,CheckNumInfos[i - 1].first_time, -1, -1, -1, k=ks / cnt))
        cnt = 1
        ks = CheckNumInfos[i].k
    if cnt >= 1:tmps.append(CheckNumInfo(-1, -1, CheckNumInfos[-1].check_time, CheckNumInfos[- 1].first_time, -1, -1, -1, k=ks / cnt))
        return tmps

def pca(x, labels, method=-1, n_clusters=-1): _pca = PCA(n_components=2)
reduced_data = _pca.fit_transform(x)
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis')
    sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], hue=labels, palette="viridis", legend="full")
    plt.title('PCA method:{} clusters: {}'.format(method, n_clusters))
    plt.xlabel('特征 1')
    plt.ylabel('特征 2')
    plt.show()
def tsne(X_high_dim, y_labels, method, n_clusters):
    tsne = TSNE(n_components=2, random_state=42)
    X_low_dim = tsne.fit_transform(X_high_dim)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X_low_dim[:, 0], y=X_low_dim[:, 1], hue=y_labels, palette="viridis", legend="full")
    plt.title("t-SNE Clustering {}".format(n_clusters))
    plt.xlabel("t-SNE Dimension 1")
    plt.ylabel("t-SNE Dimension 2")
    plt.title('TSNE method:{} clusters: {}'.format(method, n_clusters))
    plt.legend(title="Class")
    plt.show()
def k_means():
    X = get_data()
    random_state = 42
    n_clusters = 5
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(X)
    # 获取聚类结果和聚类中心
    labels = kmeans.labels_
    pca(X, labels, "K-means", n_clusters=n_clusters)
    def clean_data(x, y)
    data = list(zip(x, y))
    data = sorted(data, key=lambda x: x[0])
    z_scores_x = np.abs(stats.zscore(x))
    threshold = 3
    outliers_x = np.where(z_scores_x > threshold)
    data_cleaned = [data[i] for i in range(len(data)) if i not in outliers_x[0]]
    x_cleaned, y_cleaned = zip(*data_cleaned)
    return x_cleaned, y_cleaned
def cal_residual_by_label(ed_volume_by_lable):
    re = [] * 100
    for label, labels in enumerate(ed_volume_by_lable):
    dic = {}
    for person in labels:
    if person.id not in dic:
    id = int(person.id.split('sub')[1])
    dic[id] = [[], []]
    dic[id][1].append(person.ed_volume)
    dic[id][0].append(person.relative_time)
    else:
    dic[id][1].append(person.ed_volume)
    dic[id][0].append(person.relative_time)
    for k, v in dic.items():
    x = np.sum(np.array(v[0])) / len(v[0])
    y = np.sum(np.array(v[1])) / len(v[1])
    if label == 0:
    cal_re = a2.cal_gaussian(x, 1.798e+05, 360.1, 44.49)
    elif label == 1:
    cal_re = a2.cal_exp(x, 1.587e+04, 0.001485)
    elif label == 2:
    cal_re = a2.cal_gaussian(x, 4.367e+04, 362.5, 464.3)
    elif label == 3:
    cal_re = a2.cal_gaussian(x, 4.508e+04, 363.4, 436.1)
    re.append([k, x, y, cal_re, y - cal_re])
    def gmm():
    from sklearn.mixture import GaussianMixture
    X = get_data()
    n_components = 4
    gmm = GaussianMixture(n_components=n_components)
    # 拟合模型
    gmm.fit(X)
    labels = gmm.predict(X)
    pca(X, labels, "gmm", n_clusters=n_components)
    tsne(X, labels, "gmm", n_clusters=n_components)
    probs = gmm.predict_proba(X)

def get_method_code():
    t1 = get_table1()
    v = t1.loc[0:99, '脑室引流':'营养神经'].values.tolist()
    codes = []
    for s in v:
    s = [str(i) for i in s]
    s = ''.join(s)
    codes.append(s)
    return code
def get_data():
    at1 = a2.get_appendix_table1()
    t2 = a2.get_table2()
    t1 = a2.get_table1()
    codes = get_method_code()
    Infos = []
    for i in range(100): # 前 100 个患者
    id = t2.loc[i]['ID']
    # id 对应的下标
    index = int(id.split('sub')[1]) - 1
    repeat_num = at1.loc[index]['重复次数']
    first_time = at1.loc[index][' 入 院 首 次 检 查 时 间 点 '] - pd.Timedelta(hours=t1.loc[index]['发病到首次影像检查时间间隔'])
    first_num = at1.loc[index]['入院首次检查流水号']
    original_ed = t2.loc[i][13]
    hm_volume = t2.loc[i][2]
    method = codes[index]
    Infos.append(Info(method, at1.loc[index]['入院首次检查时间点'], first_time, original_ed, hm_volume, original_ed, original_ed, -1))
    for j in range(1, min(repeat_num, 8)):
    key = '随访' + str(j) + '流水号' check_num = t2.loc[i][key]
    check_time = at1.loc[index][at1.columns.get_loc(key) - 1]
    ed_volume = t2.loc[index][t2.columns.get_loc(key) + 12]
    if ed_volume == 0:
        break
    last_time_ed = Infos[-1].ed_volume
    Infos.append(Info(method, check_time, first_time, ed_volume, hm_volume, last_time_ed, original_ed, -1))
    x = []
    y = []
    for info in Infos:
    x.append(info.hm_volume)
    y.append(info.ed_volume)
    x, y = b2.clean_data(x, y)
    plt.scatter(x, y, c='r', cmap='viridis')
    plt.title('血肿与水肿体积关系图')
    plt.xlabel('血肿体积')
    plt.ylabel('水肿体积')
    plt.plot(x, 0.1642*np.array(x) + 2.13e+04, c='g')
    plt.legend(["y = 0.1642*x + 2.13e+04"], loc="upper right")
    plt.show()