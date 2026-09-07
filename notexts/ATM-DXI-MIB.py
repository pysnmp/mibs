#
# PySNMP MIB module ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ATM-DXI-MIB
# Source digest sha256:3c2a924ed5476028e13a7c369dfd14dd58ea2fb55bc8218fe23bb7cc4cabace0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmUniDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3))
class Dfa(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

atmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3, 2))
atmDxiConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: atmDxiConfTable.setStatus('mandatory')
atmDxiConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ATM-DXI-MIB", "atmDxiConfIfIndex"))
if mibBuilder.loadTexts: atmDxiConfEntry.setStatus('mandatory')
atmDxiConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiConfIfIndex.setStatus('mandatory')
atmDxiConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiConfMode.setStatus('mandatory')
atmDxiDFAConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: atmDxiDFAConfTable.setStatus('mandatory')
atmDxiDFAConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ATM-DXI-MIB", "atmDxiDFAConfIfIndex"), (0, "ATM-DXI-MIB", "atmDxiDFAConfDfaIndex"))
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setStatus('mandatory')
atmDxiDFAConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setStatus('mandatory')
atmDxiDFAConfDfaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 2), Dfa()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setStatus('mandatory')
atmDxiDFAConfAALType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("aal34", 3), ("aal5", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setStatus('mandatory')
atmDxiEnterprise = MibScalar((1, 3, 6, 1, 4, 1, 353, 3, 2, 4), ObjectIdentifier()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: atmDxiEnterprise.setStatus('mandatory')
mibBuilder.exportSymbols("ATM-DXI-MIB", Dfa=Dfa, atmDxi=atmDxi, atmDxiConfEntry=atmDxiConfEntry, atmDxiConfIfIndex=atmDxiConfIfIndex, atmDxiConfMode=atmDxiConfMode, atmDxiConfTable=atmDxiConfTable, atmDxiDFAConfAALType=atmDxiDFAConfAALType, atmDxiDFAConfDfaIndex=atmDxiDFAConfDfaIndex, atmDxiDFAConfEntry=atmDxiDFAConfEntry, atmDxiDFAConfIfIndex=atmDxiDFAConfIfIndex, atmDxiDFAConfTable=atmDxiDFAConfTable, atmDxiEnterprise=atmDxiEnterprise, atmForum=atmForum, atmUniDxi=atmUniDxi)
