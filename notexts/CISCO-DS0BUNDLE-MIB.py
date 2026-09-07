#
# PySNMP MIB module CISCO-DS0BUNDLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DS0BUNDLE-MIB
# Source digest sha256:64f33f8adc03e9b9a4d1a631e09c06ba45a2fdcf4d46b671baa8cd92bdc54990
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TestAndIncr")
ds0Bundle = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 32))
if mibBuilder.loadTexts: ds0Bundle.setLastUpdated('1998-05-24 20:10')
if mibBuilder.loadTexts: ds0Bundle.setOrganization('Cisco Systems, Inc.')
dsx0BundleNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 32, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0BundleNextIndex.setStatus('current')
dsx0BundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 32, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dsx0BundleTable.setStatus('current')
dsx0BundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DS0BUNDLE-MIB", "dsx0BundleIndex"))
if mibBuilder.loadTexts: dsx0BundleEntry.setStatus('current')
dsx0BundleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dsx0BundleIndex.setStatus('current')
dsx0BundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0BundleIfIndex.setStatus('current')
dsx0BundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dsx0BundleRowStatus.setStatus('current')
ds0BundleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4))
ds0BundleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1))
ds0BundleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2))
ds0BundleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2, 1)).setObjects(("CISCO-DS0BUNDLE-MIB", "ds0BundleConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleCompliance = ds0BundleCompliance.setStatus('current')
ds0BundleConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1, 2)).setObjects(("CISCO-DS0BUNDLE-MIB", "dsx0BundleNextIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleIfIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleConfigGroup = ds0BundleConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0BUNDLE-MIB", PYSNMP_MODULE_ID=ds0Bundle, ds0Bundle=ds0Bundle, ds0BundleCompliance=ds0BundleCompliance, ds0BundleCompliances=ds0BundleCompliances, ds0BundleConfigGroup=ds0BundleConfigGroup, ds0BundleConformance=ds0BundleConformance, ds0BundleGroups=ds0BundleGroups, dsx0BundleEntry=dsx0BundleEntry, dsx0BundleIfIndex=dsx0BundleIfIndex, dsx0BundleIndex=dsx0BundleIndex, dsx0BundleNextIndex=dsx0BundleNextIndex, dsx0BundleRowStatus=dsx0BundleRowStatus, dsx0BundleTable=dsx0BundleTable)
