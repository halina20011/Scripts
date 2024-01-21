local colorscheme = "tokyonight"

local statusOk, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)
if not statusOk then
    vim.notify("colorscheme " .. colorscheme .. " not found!")
    return
end
