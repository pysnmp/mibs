#
# PySNMP MIB module ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-DXI-MIB
# Produced by pysmi-1.1.12 at Mon Sep  9 10:26:52 2024
# On host fv-az735-752 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, NotificationType, MibIdentifier, Integer32, Counter64, Bits, iso, ModuleIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "Bits", "iso", "ModuleIdentity", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmUniDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3))
class Dfa(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

atmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3, 2))
atmDxiConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 2), )
if mibBuilder.loadTexts: atmDxiConfTable.setStatus('mandatory')
atmDxiConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiConfIfIndex"))
if mibBuilder.loadTexts: atmDxiConfEntry.setStatus('mandatory')
atmDxiConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiConfIfIndex.setStatus('mandatory')
atmDxiConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiConfMode.setStatus('mandatory')
atmDxiDFAConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 3), )
if mibBuilder.loadTexts: atmDxiDFAConfTable.setStatus('mandatory')
atmDxiDFAConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiDFAConfIfIndex"), (0, "ATM-DXI-MIB", "atmDxiDFAConfDfaIndex"))
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setStatus('mandatory')
atmDxiDFAConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setStatus('mandatory')
atmDxiDFAConfDfaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 2), Dfa()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setStatus('mandatory')
atmDxiDFAConfAALType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("aal34", 3), ("aal5", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setStatus('mandatory')
atmDxiEnterprise = MibScalar((1, 3, 6, 1, 4, 1, 353, 3, 2, 4), ObjectIdentifier())
if mibBuilder.loadTexts: atmDxiEnterprise.setStatus('mandatory')
mibBuilder.exportSymbols("ATM-DXI-MIB", atmDxiDFAConfTable=atmDxiDFAConfTable, atmUniDxi=atmUniDxi, atmDxiConfEntry=atmDxiConfEntry, atmDxiDFAConfEntry=atmDxiDFAConfEntry, atmDxiDFAConfDfaIndex=atmDxiDFAConfDfaIndex, atmDxiEnterprise=atmDxiEnterprise, atmForum=atmForum, atmDxiDFAConfAALType=atmDxiDFAConfAALType, atmDxiConfTable=atmDxiConfTable, atmDxiConfIfIndex=atmDxiConfIfIndex, atmDxi=atmDxi, atmDxiDFAConfIfIndex=atmDxiDFAConfIfIndex, Dfa=Dfa, atmDxiConfMode=atmDxiConfMode)
