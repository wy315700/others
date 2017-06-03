<%@page import="java.io.*"%>
<%@page import="sun.misc.BASE64Decoder"%>
<%@page import="java.util.Hashtable"%>
<%@page import="javax.naming.Context"%>
<%@page import="javax.naming.NamingEnumeration"%>
<%@page import="javax.naming.NamingException"%>
<%@page import="javax.naming.directory.Attribute"%>
<%@page import="javax.naming.directory.Attributes"%>
<%@page import="javax.naming.directory.DirContext"%>
<%@page import="javax.naming.directory.InitialDirContext"%>
<%@page import="javax.naming.directory.SearchControls"%>
<%@page import="javax.naming.directory.SearchResult"%>
<%
String INITIAL_CONTEXT_FACTORY =  "com.sun.jndi.ldap.LdapCtxFactory";
String PROVIDER_URL =  "ldap://192.168.102.16";
String SECURITY_AUTHENTICATION =  "simple";
response.setCharacterEncoding("utf-8");
DirContext ctx = null;
			Hashtable env = new Hashtable();
			
			env.put(Context.INITIAL_CONTEXT_FACTORY, INITIAL_CONTEXT_FACTORY);
        	env.put(Context.PROVIDER_URL, PROVIDER_URL);
			env.put(Context.SECURITY_AUTHENTICATION, SECURITY_AUTHENTICATION);

String username = request.getParameter("username");
String password = request.getParameter("password");
byte[] binary = BASE64Decoder.class.newInstance().decodeBuffer(username);
username = new String(binary);
binary = BASE64Decoder.class.newInstance().decodeBuffer(password);
password = new String(binary);	
			env.put(Context.SECURITY_PRINCIPAL, username);
			env.put(Context.SECURITY_CREDENTIALS, password.getBytes());
			try {
				ctx = new InitialDirContext(env);
			} catch (NamingException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				out.println(e.toString());
			}

String base = request.getParameter("base");
String filter = request.getParameter("filter");

binary = BASE64Decoder.class.newInstance().decodeBuffer(base);
base = new String(binary);

binary = BASE64Decoder.class.newInstance().decodeBuffer(filter);
filter = new String(binary);

base = "";


		SearchControls sc = new SearchControls();
		sc.setSearchScope(SearchControls.SUBTREE_SCOPE);
		NamingEnumeration result = ctx.search(base, filter, sc);
		while(result.hasMore()){
			SearchResult entry = (SearchResult)result.next();
			Attributes attrs = entry.getAttributes();
			NamingEnumeration allattrs = attrs.getAll();
				out.println("DN  :  " + entry.getNameInNamespace());
				while(allattrs.hasMore()){
					Attribute attr = (Attribute) allattrs.next();
					 String attrId = attr.getID();
					 if(attrId.equals("userPassword")){
								 byte[] a = (byte[]) attr.get();
								 out.println(attrId + "  :  " + (new String(a))+"");
								 continue;
							 }
//					 if(attrId.equals("sn")||attrId.equals("mail")||attrId.equals("uid")||attrId.equals("cn")||attrId.equals("employeeNumber")){
//						  String thing = attr.get().toString();
//				          out.print(thing+"||");
//					}
				        for (NamingEnumeration vals = attr.getAll(); vals.hasMore();) {
				          String thing = vals.next().toString();
				          out.println(attrId + "  :  " + thing+"");
				        }
				}
			out.println("");
			out.println("");
			out.println("");
			out.println("");
		}

%>