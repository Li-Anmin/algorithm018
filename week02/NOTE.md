学习笔记
Java——HashMap

----------
哈希表的主干就是数组

----------
HashMap即是采用了链地址法，也就是数组+链表的方式。数组是HashMap的主体，链表则是主要为了解决哈希冲突而存在的，如果定位到的数组位置不含链表（当前entry的next指向null）,那么查找，添加等操作很快，仅需一次寻址即可；如果定位到的数组包含链表，对于添加操作，其时间复杂度为O(n)，首先遍历链表，存在即覆盖，否则新增；对于查找操作来讲，仍需遍历链表，然后通过key对象的equals方法逐一比对查找。所以，性能考虑，HashMap中的链表出现越少，性能才会越好。

----------
Hashmap用法

    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map.Entry;
    
    public class HashMapTest {
    
    	public static void main(String[] args) {
    		HashMap<String, String> map = new HashMap<>();
    		map.put("zhang", "31");//存放键值对
    
    		System.out.println(map.containsKey("zhang"));//键中是否包含这个数据
    		System.out.println(map.containsKey("daniu"));
    		System.out.println("=========================");
    
    		System.out.println(map.get("zhang"));//通过键拿值
    		System.out.println(map.get("daniu"));
    		System.out.println("=========================");
    
    		System.out.println(map.isEmpty());//判空
    		System.out.println(map.size());
    		System.out.println("=========================");
    
    		System.out.println(map.remove("zhang"));//从键值中删除
    		System.out.println(map.containsKey("zhang"));
    		System.out.println(map.get("zhang"));//获取值
    		System.out.println(map.isEmpty());
    		System.out.println(map.size());
    		System.out.println("=========================");
    
    		map.put("zhang", "31");
    		System.out.println(map.get("zhang"));
    		map.put("zhang", "32");
    		System.out.println(map.get("zhang"));
    		System.out.println("=========================");
    
    		map.put("zhang", "31");
    		map.put("cheng", "32");
    		map.put("yun", "33");
    
    		for (String key : map.keySet()) {
    			System.out.println(key);
    		}
    		System.out.println("=========================");
    
    		for (String values : map.values()) {
    			System.out.println(values);
    		}
    		System.out.println("=========================");
    
    		map.clear();
    		map.put("A", "1");
    		map.put("B", "2");
    		map.put("C", "3");
    		map.put("D", "1");
    		map.put("E", "2");
    		map.put("F", "3");
    		map.put("G", "1");
    		map.put("H", "2");
    		map.put("I", "3");
    		for (Entry<String, String> entry : map.entrySet()) {
    			String key = entry.getKey();
    			String value = entry.getValue();
    			System.out.println(key + "," + value);
    		}
    		System.out.println("=========================");
    
    		// you can not remove item in map when you use the iterator of map
    		// for(Entry<String,String> entry : map.entrySet()){
    		// if(!entry.getValue().equals("1")){
    		// map.remove(entry.getKey());
    		// }
    		// }
    
    		// if you want to remove items, collect them first, then remove them by
    		// this way.
    		List<String> removeKeys = new ArrayList<String>();
    		for (Entry<String, String> entry : map.entrySet()) {
    			if (!entry.getValue().equals("1")) {
    				removeKeys.add(entry.getKey());
    			}
    		}
    		for (String removeKey : removeKeys) {
    			map.remove(removeKey);
    		}
    		for (Entry<String, String> entry : map.entrySet()) {
    			String key = entry.getKey();
    			String value = entry.getValue();
    			System.out.println(key + "," + value);
    		}
    		System.out.println("=========================");
    
    	}
    
    }


