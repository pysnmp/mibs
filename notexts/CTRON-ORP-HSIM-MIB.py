#
# PySNMP MIB module CTRON-ORP-HSIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ORP-HSIM-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:11:03 2024
# On host fv-az2021-432 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ctOrpHSIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctOrpHSIM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Integer32, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Counter64, ObjectIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Integer32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter64", "ObjectIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

ctOrpHSIMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1), )
if mibBuilder.loadTexts: ctOrpHSIMTable.setStatus('mandatory')
ctOrpHSIMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1), ).setIndexNames((0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMSlot"), (0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMIndex"))
if mibBuilder.loadTexts: ctOrpHSIMEntry.setStatus('mandatory')
ctOrpHSIMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMSlot.setStatus('mandatory')
ctOrpHSIMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIndex.setStatus('mandatory')
ctOrpHSIMIfRef = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMIfRef.setStatus('mandatory')
ctOrpHSIMMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctOrpHSIMMACAddress.setStatus('mandatory')
ctOrpHSIMIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMIPAddress.setStatus('mandatory')
ctOrpHSIMSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSubnetMask.setStatus('mandatory')
ctOrpHSIMROCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMROCommName.setStatus('mandatory')
ctOrpHSIMRWCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMRWCommName.setStatus('mandatory')
ctOrpHSIMSUCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctOrpHSIMSUCommName.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ORP-HSIM-MIB", ctOrpHSIMSubnetMask=ctOrpHSIMSubnetMask, MacAddress=MacAddress, ctOrpHSIMIfRef=ctOrpHSIMIfRef, ctOrpHSIMTable=ctOrpHSIMTable, ctOrpHSIMMACAddress=ctOrpHSIMMACAddress, ctOrpHSIMIndex=ctOrpHSIMIndex, ctOrpHSIMIPAddress=ctOrpHSIMIPAddress, ctOrpHSIMEntry=ctOrpHSIMEntry, ctOrpHSIMSlot=ctOrpHSIMSlot, ctOrpHSIMRWCommName=ctOrpHSIMRWCommName, ctOrpHSIMROCommName=ctOrpHSIMROCommName, ctOrpHSIMSUCommName=ctOrpHSIMSUCommName)
