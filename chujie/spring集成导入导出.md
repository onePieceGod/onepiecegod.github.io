#spring集成导入导出
> 1.添加pom依赖
>>
  		<dependency>
            <groupId>com.github.liaochong</groupId>
            <artifactId>myexcel</artifactId>
            <version>2.8.5</version>
            <exclusions>
                <exclusion>
                    <groupId>org.apache.poi</groupId>
                    <artifactId>poi-ooxml</artifactId>
                </exclusion>
            </exclusions>
        </dependency>


>2.在实体上添加注解
		
		import com.github.liaochong.myexcel.core.annotation.ExcelColumn;
		import com.github.liaochong.myexcel.core.annotation.ExcelTable;
		import com.github.liaochong.myexcel.core.annotation.ExcludeColumn;

>> @ExcelTable注解
>
>sheetName：导出时工作簿名称，excludeParent：导出时排除父类的字段

>> @ExcludeColumn 
>
>字段注解，导出时排除改字段

>> @ExcelColumn 字段注解
>
 * title：导出时字段的标题名称
 * order：导出时字段顺序，从0开始
 * index：导入时对应excel的列顺序，从0开始
 * groups：导出时使用，当前字段所属分组，构建时根据传入的分组选择导出的字段

##导入导出操作
> 模板下载

	public void excelTemplateDownload(HttpServletResponse response, String name, 	List<String> titles) {
        Workbook workbook = DefaultExcelBuilder.getInstance()
                .sheetName(name)
                .titles(titles)
                .build(new ArrayList());
        AttachmentExportUtil.export(workbook, name, response);
    }
> 导入(获得导入的实体列表)

	public List<T> excelImp(HttpServletRequest request, Class<T> clazz) throws Exception {
        try {
            List<T> list = new ArrayList<T>();
            CommonsMultipartResolver resolver = new CommonsMultipartResolver();
            if (resolver.isMultipart(request)) {
                MultipartHttpServletRequest multipartRequest = (MultipartHttpServletRequest) request;
                int size = multipartRequest.getMultiFileMap().size();
                MultiValueMap<String, MultipartFile> multiValueMap = multipartRequest.getMultiFileMap();
                if (multiValueMap != null && size > 0) {
                    for (MultiValueMap.Entry<String, List<MultipartFile>> entry : multiValueMap.entrySet()) {
                        List<MultipartFile> multipartFileList = entry.getValue();
                        for (MultipartFile multipartFile : multipartFileList) {
                            list = SaxExcelReader.of(clazz)
                                    .rowFilter(row -> row.getRowNum() > 0) // 如无需过滤，可省略该操作，0代表第一行
                                    .read(multipartFile.getInputStream());// 可接收inputStream
                        }
                    }
                }
            }
            return list;
        } catch (IOException e) {
            throw new Exception(e);
        }
    }

> 导出

 
	public void exportExcel(HttpServletResponse response, String name, List<T> data, Class<T> clazz) {
        Workbook workbook = DefaultExcelBuilder.of(clazz).workbookType(WorkbookType.SXLSX).rowAccessWindowSize(100)
                .build(data);
        AttachmentExportUtil.export(workbook, name, response);
    }

##控制器导入导出
>模板下载

 	/**
     * Excel模板下载
     */
    @ApiOperation(value = "Excel模板下载", tags = "READ", response = Supplier.class)
    @RequestMapping(value = "/excelTemplateDownload", method = {RequestMethod.GET, RequestMethod.POST})
    public void excelTemplateDownload(HttpServletRequest request, HttpServletResponse response) {
        try {
            List<String> titles = new ArrayList<>();
            titles.add("供应商名称");
            titles.add("所属组织编码");

            super.excelTemplateDownload(response, "供应商导入模板", titles);
        } catch (Exception e) {
            logger.error("Excel模版下载失败", e);
        }
    }

> 模板导入

 	/**
     * Excel导入
     */
    @ApiOperation(value = "导入", tags = "READ", response = Supplier.class)
    @RequestMapping(value = "/excelImp", method = {RequestMethod.GET, RequestMethod.POST})
    @ResponseBody
    public Map<String, Object> excelImp(HttpServletRequest request, HttpServletResponse response) {
        Map<String, Object> result = new HashMap<>();
        try {
            List<Supplier> list = super.excelImp(request, Supplier.class);
            String msg = this.supplierService.checkImport(list);
            result.put("status", 1);
            result.put("data", msg);
        } catch (
                Exception e) {
            e.printStackTrace();
            response.setStatus(500);
        }
        return result;
    }
 
> 数据导出

 	/**
     * Excel导出
     */
    @ApiOperation(value = "Excel导出", tags = "READ", response = Supplier.class)
    @RequestMapping(value = "/exportExcel", method = {RequestMethod.GET, RequestMethod.POST})
    public void exportExcel(HttpServletResponse response, PageRequest pageRequest, @FrontModelExchange(modelType = Supplier.class) SearchParams searchParams) {
        try {
            Map<String, Object> searchMap = searchParams.getSearchMap();

            List<Supplier> data = this.supplierService.queryList(searchMap);

            super.exportExcel(response, "供应商", data, Supplier.class);
        } catch (Exception e) {
            logger.error("Excel导出失败", e);
        }
    }