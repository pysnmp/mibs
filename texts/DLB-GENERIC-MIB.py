#
# PySNMP MIB module DLB-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLB-GENERIC-MIB
# Source digest sha256:1b2a4d4691199bfed3f194914b673edefd4d599bae8b047824adc3ca57e8a60c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlbGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 1))
dlbGenericMIB.setRevisions(('2009-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlbGenericMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: dlbGenericMIB.setLastUpdated('2009-02-13 00:00')
if mibBuilder.loadTexts: dlbGenericMIB.setOrganization('Deliberant')
if mibBuilder.loadTexts: dlbGenericMIB.setContactInfo('\n        Deliberant Customer Support\n        E-mail: support@deliberant.com')
if mibBuilder.loadTexts: dlbGenericMIB.setDescription('The Deliberant Generic MIB.')
dlbGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1))
dlbGenericNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0))
dlbGenericInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1))
dlbPowerLoss = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbPowerLoss.setStatus('current')
if mibBuilder.loadTexts: dlbPowerLoss.setDescription('This notification is sent on device boot after power loss or device crash.')
dlbAdministrativeReboot = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbAdministrativeReboot.setStatus('current')
if mibBuilder.loadTexts: dlbAdministrativeReboot.setDescription('This notification is sent on device boot after administrator rebooted device.')
mibBuilder.exportSymbols("DLB-GENERIC-MIB", PYSNMP_MODULE_ID=dlbGenericMIB, dlbAdministrativeReboot=dlbAdministrativeReboot, dlbGenericInfo=dlbGenericInfo, dlbGenericMIB=dlbGenericMIB, dlbGenericMIBObjects=dlbGenericMIBObjects, dlbGenericNotifs=dlbGenericNotifs, dlbPowerLoss=dlbPowerLoss)
