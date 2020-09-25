 <template>
  <div>
    <div>
      <el-button
        icon="el-icon-plus"
        size="mini"
        type="primary"
        style="float:right;margin:10px"
        @click="dialogFormVisible=true"
      >新增</el-button>
    </div>
    <el-table
      :data="tableData"
      size="mini"
      stripe
      :header-cell-style="{background:'#0747A6',color:'#F8F9FA'}"
    >
      <el-table-column v-for="heade in heades" :key="heade" :prop="heade.prop" :label="heade.label"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            icon="el-icon-edit"
            size="mini"
            type="primary"
            @click="handleEdit(scope.$index, scope.row)"
          ></el-button>
          <el-button
            icon="el-icon-delete"
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
          ></el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="title" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item v-for="item in heades" :key="item" :label="item.label" label-width="120px">
          <el-input v-model="from[item.prop]" style="width:300px" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addcase()">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      heades: [
        {
          prop: "name",
          label: "用例名称",
        },
        {
          prop: "module",
          label: "所属模块",
        },
        {
          prop: "step",
          label: "操作步骤",
        },
        {
          prop: "result",
          label: "预期结果",
        },
        {
          prop: "grade",
          label: "用例等级",
        },
        {
          prop: "execution",
          label: "执行状态",
        },
        {
          prop: "cover",
          label: "覆盖状态",
        },
      ],
      tableData: [],
      dialogFormVisible: false,
      title: "新增用例",
      from: {},
    };
  },
  mounted: function () {
    this.getdata();
  },
  methods: {
    getdata() {
      this.$ajax.get("api/case/?format=json", { 
        headers: {
            'Authorization': 'Token '+JSON.parse(localStorage.getItem("Authorization")),
        }
      }).then((res) => {
        this.tableData = res.data;
      });
    },
    addcase() {
      this.$ajax
        .post(
          "api/case/?format=json",
         {
            from:this.from 
            }
        )
        .then((res) => {
          this.$message({
            message: "成功",
            type: "success",
          });
          this.dialogFormVisible=false;
        });
    },
  },
};
</script>