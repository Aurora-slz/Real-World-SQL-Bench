import json
import sqlite3
import os

def build_info_tree(base_dir=r"local_sqlite"):
    db_path = os.path.join(base_dir, "complex_oracle.sqlite")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()  

    # Step 0: Initialize the tree
    tree = []

        # Step 1: Get all the cust_id values from the sales table
    # ['prod_id', 'cust_id', 'time_id', 'channel_id', 'promo_id', 'quantity_sold', 'amount_sold']
    cursor.execute("PRAGMA table_info(sales)")
    sales_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    sales_num2header = {v: k for k, v in sales_header2num.items()}

    cursor.execute("SELECT * FROM sales")
    sales_data = cursor.fetchall()
    # (prod_id, time_id, promo_id, channel_id) -> sale_row
    sales_ids2row = {(row[sales_header2num['cust_id']], row[sales_header2num['prod_id']], row[sales_header2num['time_id']], row[sales_header2num['promo_id']], row[sales_header2num['channel_id']]): row for row in sales_data}
    
    cust_ids = list(set([row[sales_header2num['cust_id']] for row in sales_data]))    # Get unique cust_id values

    # Initialize the tree with cust_id as keys
    tree = [{"cust_id": cust_id, "customer_info": {}, "trade": []} for cust_id in cust_ids] 
    # cust_id -> idx
    tree_custid2idx = {d['cust_id']: n for d, n in zip(tree, range(len(tree)))}

    ##############################################################################################################

    # Step 2: Get all the users' information from `customers`, `supplementary_demographics` 
    # and `countries` tables

    # SubStep 2.1: Get all the customers information from `customers` table
    # ['cust_id', 'cust_first_name', 'cust_last_name', 'cust_gender', 'cust_year_of_birth', 'cust_marital_status', 
    # 'cust_street_address', 'cust_postal_code', 'cust_city', 'cust_city_id', 'cust_state_province', 
    # 'cust_state_province_id', 'country_id', 'cust_main_phone_number', 'cust_income_level', 'cust_credit_limit', 
    # 'cust_email', 'cust_total', 'cust_total_id', 'cust_src_id', 'cust_eff_from', 'cust_eff_to', 'cust_valid']
    cursor.execute("PRAGMA table_info(customers)")
    cust_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    cust_num2header = {v: k for k, v in cust_header2num.items()}

    cursor.execute("SELECT * FROM customers")   # Get all the customers data
    customers_data = cursor.fetchall()

    # SubStep 2.2: Get all the supplementary demographics information from `supplementary_demographics` table
    # ['cust_id', 'education', 'occupation', 'household_size', 'yrs_residence', 'affinity_card', 
    # 'cricket', 'baseball', 'tennis', 'soccer', 'golf', 'unknown', 'misc', 'comments']
    cursor.execute("PRAGMA table_info(supplementary_demographics)")
    supp_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    supp_num2header = {v: k for k, v in supp_header2num.items()}

    cursor.execute("SELECT * FROM supplementary_demographics")  # Get all the `supplementary demographics` data
    supp_data = cursor.fetchall()
    # `supplementary_demographics`中的cust_id
    supp_cust_ids = [row[supp_header2num['cust_id']] for row in supp_data]  

    # SubStep 2.3: Get all the countries information from `countries` table
    # ['country_id', 'country_iso_code', 'country_name', 'country_subregion', 'country_subregion_id', 
    # 'country_region', 'country_region_id', 'country_total', 'country_total_id']
    cursor.execute("PRAGMA table_info(countries)")
    country_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    country_num2header = {v: k for k, v in country_header2num.items()}
    
    cursor.execute("SELECT * FROM countries")  # Get all the `countries` data
    countries_data = cursor.fetchall()
    # `countries`中的country_id
    country_ids = [row[country_header2num['country_id']] for row in countries_data]

        ##############################################################################################################

    # Step 4: Get all the information from products bought from customers

    # SubStep 4.1: Get all the `prod_id` for each `cust_id` from `sales` table
    # ['prod_id', 'prod_name', 'prod_desc', 'prod_subcategory', 'prod_subcategory_id', 'prod_subcategory_desc', 
    # 'prod_category', 'prod_category_id', 'prod_category_desc', 'prod_weight_class', 'prod_unit_of_measure', 
    # 'prod_pack_size', 'supplier_id', 'prod_status', 'prod_list_price', 'prod_min_price', 'prod_total', '
    # prod_total_id', 'prod_src_id', 'prod_eff_from', 'prod_eff_to', 'prod_valid']
    cursor.execute("PRAGMA table_info(products)")
    prod_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    prod_num2header = {v: k for k, v in prod_header2num.items()}

    cursor.execute("SELECT * FROM products")  # Get all the `products` data
    products_data = cursor.fetchall()
    prod_ids = [row[prod_header2num['prod_id']] for row in products_data]  # Get all the prod_id values
    # prod_ids不连续, 需要通过键值对快速根据prod_id获取对应的行数据
    prod_id2row = {row[prod_header2num['prod_id']]: row for row in products_data}

    # SubStep 4.2: Get all the channel information from `channels` table
    cursor.execute("PRAGMA table_info(channels)")
    channel_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    channel_num2header = {v: k for k, v in channel_header2num.items()}

    cursor.execute("SELECT * FROM channels")  # Get all the `channels` data
    channels_data = cursor.fetchall()
    channel_ids = [row[channel_header2num['channel_id']] for row in channels_data]  # Get all the channel_id values
    # channel_ids不连续, 需要通过键值对快速根据channel_id获取对应的行数据
    channel_id2row = {row[channel_header2num['channel_id']]: row for row in channels_data}

    # SubStep 4.3: Get all the time information from `times` table
    cursor.execute("PRAGMA table_info(times)")
    time_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    time_num2header = {v: k for k, v in time_header2num.items()}

    cursor.execute("SELECT * FROM times")  # Get all the `times` data
    times_data = cursor.fetchall()
    time_ids = [row[time_header2num['time_id']] for row in times_data]  # Get all the time_id values
    # times_id(如2019-01-01)与id没有直接关系, 需要通过键值对快速根据time_id获取对应的行数据
    time_id2row = {row[time_header2num['time_id']]: row for row in times_data}  # Map time_id to row data

    # SubStep 4.4: Get all the promotion information from `promotions` table
    cursor.execute("PRAGMA table_info(promotions)")
    promotion_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    promotion_num2header = {v: k for k, v in promotion_header2num.items()}

    cursor.execute("SELECT * FROM promotions")
    promotions_data = cursor.fetchall()
    promo_ids = [row[promotion_header2num['promo_id']] for row in promotions_data]
    promotion_id2row = {row[promotion_header2num['promo_id']]: row for row in promotions_data}
    ##############################################################################################################

    # Step 5: Get all the information from `sales`, `costs` and `profits`(sales在前面已导出)
    cursor.execute("PRAGMA table_info(costs)")
    cost_header2num = {column[1]: column[0] for column in cursor.fetchall()}
    cost_num2header = {v: k for k, v in cost_header2num.items()}

    cursor.execute("SELECT * FROM costs")
    costs_data = cursor.fetchall()
    # (prod_id, time_id, promo_id, channel_id) -> cost_row
    costs_ids2row = {(row[cost_header2num['prod_id']], row[cost_header2num['time_id']], row[cost_header2num['promo_id']], row[cost_header2num['channel_id']]): row for row in costs_data}
    
    # with open(r"local_sqlite\profits_202506131754.json", "r") as f:     # 318674条数据
    #     profits_data = json.load(f)
    # profits_data = profits_data["profits"]
    # profit_ids2row = {(row["cust_id"], row["prod_id"], row["time_id"], row["promo_id"], row["channel_id"]): row for row in profits_data}

    ##############################################################################################################

    # build the tree structure on the `customer information` side
    for row in customers_data:                          # 遍历customers表中的每一行数据
        cust_id = row[cust_header2num['cust_id']]       # customers中可能会有sales中不存在的id

        if cust_id not in tree_custid2idx.keys():                  # 如果cust_id不在sales中存在，则跳过(移除了不在sales中的用户)
            continue
        
        idx = tree_custid2idx[cust_id]                  # 获取tree中对应的索引
        # 插入`customers`表中的数据到tree中的某个用户树下
        tree[idx]["customer_info"] = {cust_num2header[i]: row[i] for i in range(1, len(row))}
        
        # 插入`supplementary_demographics`表中的数据到tree中的某个用户下的customer_info下
        if cust_id in supp_cust_ids:                    # 只有cust_id在supplementary_demographics中存在时才添加
            supp_row = supp_data[cust_id - 100001]      # supp_data中的cust_id从100001开始
            tree[idx]["customer_info"]["supplementary_info"] = {supp_num2header[i]: supp_row[i] for i in range(1, len(supp_row))} 
        else:
            tree[idx]["customer_info"]["supplementary_info"] = None  

        # 插入`countries`表中的数据到tree中的某个用户下的customer_info下
        country_id = row[cust_header2num['country_id']] # 获取当前行的country_id
        if country_id in country_ids:                   # 只有country_id在countries中存在时才添加
            country_row = countries_data[country_id - 52769]    # countries_data中的country_id从52769开始
            # 插入country信息
            tree[idx]["customer_info"]["country_info"] = {country_num2header[i]: country_row[i] for i in range(0, len(country_row))}    
        else:
            tree[idx]["customer_info"]["country_info"] = None

    ##############################################################################################################
    
    # build the tree structure on the `product information` side
    for row in sales_data:  # 遍历sales表中的每一行数据
        cust_id = row[sales_header2num['cust_id']]
        idx = tree_custid2idx[cust_id]  # 获取tree中对应的索引
        prod_id = row[sales_header2num['prod_id']]
        channel_id = row[sales_header2num['channel_id']]
        time_id = row[sales_header2num['time_id']]
        promo_id = row[sales_header2num['promo_id']]

        trade_list = tree[idx]["trade"]

        # 把sales中的每条记录整理成new_row的形式, 插入到当前cust_id对应的字典下的trade字段中
        new_row = {"sales_info": {}, "costs_info": {}, "reference": {}}   

        sales_info = new_row["sales_info"]
        costs_info = new_row["costs_info"]
        reference = new_row["reference"]

        # 插入`products`表中的数据到tree中的某个用户下的trade列表中
        if prod_id in prod_ids:         # 会存在不在`products`表中的prod_id, 此时对应的prod_id: {}值为空
            prod_row = prod_id2row[prod_id]  # 获取当前prod_id对应的行数据
            reference["product_info"] = {prod_num2header[i]: prod_row[i] for i in range(0, len(prod_row))}
        else:
            reference["product_info"] = None

        # 插入`times`表中的数据到tree中的某个用户下的trade列表中
        if time_id in time_ids:
            time_row = time_id2row[time_id]
            reference["time_info"] = {time_num2header[i]: time_row[i] for i in range(0, len(time_row))}
        else:
            reference["time_info"] = None
        
        # 插入`channels`表中的数据到tree中的某个用户下的trade列表中
        if channel_id in channel_ids:
            channel_row = channel_id2row[channel_id]
            reference["channel_info"] = {channel_num2header[i]: channel_row[i] for i in range(0, len(channel_row))}
        else:
            reference["channel_info"] = None    

        # 插入`promotions`表中的数据到tree中的某个用户下的trade列表中
        if promo_id in promo_ids:
            promo_row = promotion_id2row[promo_id]
            reference["promotion_info"] = {promotion_num2header[i]: promo_row[i] for i in range(0, len(promo_row))}
        else:
            reference["promotion_info"] = None    

        sales_row = sales_ids2row.get((cust_id, prod_id, time_id, promo_id, channel_id), None)
        if sales_row is not None:
            sales_info["quantity_sold"] = sales_row[sales_header2num['quantity_sold']]
            sales_info["amount_sold"] = sales_row[sales_header2num['amount_sold']]
        else:
            new_row["sales_info"] = None    # 注意这里不能是sales_info = None, 这会导致sales_info重新被赋值,
                                            # 从而不再是new_row["sales_info"]的引用. 下面costs_info同理

        costs_row = costs_ids2row.get((prod_id, time_id, promo_id, channel_id), None)
        if costs_row is not None:
            costs_info["unit_cost"] = costs_row[cost_header2num["unit_cost"]]
            costs_info["unit_price"] = costs_row[cost_header2num["unit_price"]]
        else:
            new_row["costs_info"] = None

        trade_list.append(new_row)


    with open("example_V2_cust_id_2.json", "w", encoding="utf-8") as f:
        json.dump(tree[tree_custid2idx[2]], f, indent=4)

    with open("example_V2_cust_id_513.json", "w", encoding="utf-8") as f:
        json.dump(tree[tree_custid2idx[513]], f, indent=4)
    
    with open("example_V2_cust_id_100001.json", "w", encoding="utf-8") as f:
        json.dump(tree[tree_custid2idx[100001]], f, indent=4)

    with open("tree_V2.jsonl", "w", encoding="utf-8") as f:
        for info in tree:       # info是字典, 键为cust_id, customer_info和trade
            json_line = json.dumps(info, ensure_ascii=False)
            f.write(json_line + "\n")

    #print(tree[100001])
    print("Finished.")

if __name__ == "__main__":
    build_info_tree()
    