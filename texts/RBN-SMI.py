#
# PySNMP MIB module RBN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-SMI
# Produced by pysmi-1.1.12 at Wed Sep 18 06:45:22 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Unsigned32, Bits, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Integer32, ModuleIdentity, IpAddress, enterprises, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Integer32", "ModuleIdentity", "IpAddress", "enterprises", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnSMI = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352))
rbnSMI.setRevisions(('2011-01-19 18:00', '2002-06-06 00:00', '2001-06-27 00:00', '1998-04-18 23:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnSMI.setRevisionsDescriptions(('Update CONTACT-INFO & ORGANIZATION. ', 'Updated Contact-info and recovered revision info.', 'Added rbnInternal.', 'Initial version.',))
if mibBuilder.loadTexts: rbnSMI.setLastUpdated('201101191800Z')
if mibBuilder.loadTexts: rbnSMI.setOrganization('Ericsson AB.')
if mibBuilder.loadTexts: rbnSMI.setContactInfo('       Ericsson AB.\n\n                Postal: 100 Headquarters Dr\n                        San Jose, CA  95134\n                        USA\n\n                 Phone: +1 408 750 5000\n                   Fax: +1 408 750 5599\n                ')
if mibBuilder.loadTexts: rbnSMI.setDescription('The Structure of Management Information for\n\t\tthe enterprise.')
rbnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 1))
if mibBuilder.loadTexts: rbnProducts.setStatus('current')
if mibBuilder.loadTexts: rbnProducts.setDescription('')
rbnMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 2))
if mibBuilder.loadTexts: rbnMgmt.setStatus('current')
if mibBuilder.loadTexts: rbnMgmt.setDescription('')
rbnExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 3))
if mibBuilder.loadTexts: rbnExperiment.setStatus('current')
if mibBuilder.loadTexts: rbnExperiment.setDescription('')
rbnCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 4))
if mibBuilder.loadTexts: rbnCapabilities.setStatus('current')
if mibBuilder.loadTexts: rbnCapabilities.setDescription('')
rbnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 5))
if mibBuilder.loadTexts: rbnModules.setStatus('current')
if mibBuilder.loadTexts: rbnModules.setDescription('')
rbnEntities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 6))
if mibBuilder.loadTexts: rbnEntities.setStatus('current')
if mibBuilder.loadTexts: rbnEntities.setDescription('')
rbnInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 7))
if mibBuilder.loadTexts: rbnInternal.setStatus('current')
if mibBuilder.loadTexts: rbnInternal.setDescription('')
mibBuilder.exportSymbols("RBN-SMI", rbnExperiment=rbnExperiment, rbnMgmt=rbnMgmt, rbnSMI=rbnSMI, rbnCapabilities=rbnCapabilities, PYSNMP_MODULE_ID=rbnSMI, rbnEntities=rbnEntities, rbnInternal=rbnInternal, rbnProducts=rbnProducts, rbnModules=rbnModules)
