// ROOT macro (interpreted C++)
//
// Reads histogram from file and does some graphics customizations 
// to make more presentable
//

void plot(string hist="hgau", string hdescriptor="Gaussian", float ymin=0.0, 
          float ymax=1800.0, float xlmin=0.15, float ylmin=0.75){

TCanvas *c1 = new TCanvas("c1","multipads",800,600);
TFile *f = new TFile("histos-random.root");

TH1D * h = (TH1D*)f->Get(hist.c_str());
h->GetYaxis()->SetTitleOffset(1.4);
h->SetMinimum(ymin);
h->SetMaximum(ymax);

c1->SetTicks(1,1);
c1->SetGrid();

h->SetLineColor(kBlue);
h->SetLineWidth(2);
h->SetTitle("Probability distributions using random numbers");
h->GetXaxis()->SetTitle("Random variate value");
h->GetYaxis()->SetTitle("Random variates per bin");
h->Draw("ehist");
gPad->Update();

// Statistics box
gStyle->SetOptStat("nemr");   // See https://root.cern/doc/v608/classTPaveStats.html
TPaveStats *st = (TPaveStats*)h->FindObject("stats");
st->SetLineColor(kBlue);
st->SetTextColor(kBlue);
st->SetStatFormat("8.6g");
h->Draw("ehist");

// Add a legend
const float dx=0.25;
const float dy=0.1;
TLegend* leg = new TLegend(xlmin,ylmin,xlmin+dx,ylmin+dy);
leg->SetTextFont(42);
leg->SetTextSize(0.05);
leg->AddEntry(h,hdescriptor.c_str(),"l");
leg->SetBorderSize(1);                          // Include border
leg->Draw();

c1->Print("Plot.pdf");

}
